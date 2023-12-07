import json
import subprocess
import os
import logging
import argparse
from multiprocessing import Pool

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_docker_image(image_config, output_directory, failed_images):
    try:
        image_id = image_config.get("id")

        # Check for failed images
        if len(failed_images) != 0:
            if image_id not in failed_images:
                return

        cli_args = image_config.get("cli-args",)

        # Build the Docker command
        docker_command = ["docker", "run", "--rm"]

        # Add the command line args
        docker_command.extend(cli_args)

        # Run the Docker image
        subprocess.run(docker_command, check=True)

    except Exception as e:
        logging.error(f"Error running {image_id}: {str(e)}")

        # Mark the image as failed
        with open("failed_images.txt", "a") as failed_file:
            failed_file.write(f"{image_id}\n")

# find and replace all placeholders with the values
def replace_json_placeholders(json_str, values): 
    for k, v in values.items():
        placeholder = "<%s>" % k
        json_str = json_str.replace(placeholder, v)

    return json_str

def main(config_file):
    try:
        with open(config_file, "r") as f:
            config = json.load(f)
        values = config.get("values")

        with open(config_file, "r") as f:
            config_string = f.read()

        config_string = replace_json_placeholders(config_string, values)
        config = json.loads(config_string)

        images = config.get("images", [])
        output_directory = config['values']['output_directory']
        print(output_directory)

        # Load the list of completed images
        failed_images = set()
        if os.path.isfile("failed_images.txt"):
            with open("failed_images.txt", "r") as failed_file:
                failed_images = set(failed_file.read().splitlines())
            # Clear the failed images file
            with open("failed_images.txt", "w") as failed_file:
                pass

        # Create a Pool to run Docker images in parallel
        pool = Pool(processes=len(images))
        pool.starmap(run_docker_image, [(image, output_directory, failed_images) for image in images])
        pool.close()
        pool.join()

    except FileNotFoundError:
        logging.error(f"Config file '{config_file}' not found.")
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in '{config_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Docker images based on a JSON configuration file.")
    parser.add_argument("config_file", help="Path to the JSON configuration file")

    args = parser.parse_args()
    main(args.config_file)

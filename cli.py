import json
import subprocess
import os
import logging
import argparse
from multiprocessing import Pool

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_docker_image(image_config, output_directory, completed_images):
    try:
        image_id = image_config.get("id")

        # Check if the image has already been completed
        if image_id in completed_images:
            logging.info(f"{image_id} already completed.")
            return

        cli_args = image_config.get("cli-args",)

        # Build the Docker command
        docker_command = ["docker", "run", "--rm"]

        # Add the command line args
        docker_command.extend(cli_args)

        # Run the Docker image
        subprocess.run(docker_command, check=True)

        # Move the output file to the specified output directory
        output_file = docker_command[-1]  # Get the last argument (output file)
        output_file_path = os.path.join(output_directory, output_file)
        os.rename(output_file, output_file_path)

        # Mark the image as completed
        completed_images.add(image_id)
        with open("completed_images.txt", "a") as completed_file:
            completed_file.write(f"{image_id}\n")

        logging.info(f"{image_id} completed successfully.")
    except Exception as e:
        logging.error(f"Error running {image_id}: {str(e)}")

# find and replace all placeholders with the values
def replace_json_placeholders(json_str, values): 
    for k, v in values.items():
        placeholder = "<%s>" % k
        json_str = json_str.replace(placeholder, v)

    return json_str

def process_image(image_config, output_directory, completed_images):
    run_docker_image(image_config, output_directory, completed_images)

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
        output_directory = config.get("output-directory")

        # Load the list of completed images
        completed_images = set()
        if os.path.isfile("completed_images.txt"):
            with open("completed_images.txt", "r") as completed_file:
                completed_images = set(completed_file.read().splitlines())

        # Create a Pool to run Docker images in parallel
        pool = Pool(processes=len(images))
        pool.starmap(process_image, [(image, output_directory, completed_images) for image in images])
        pool.close()
        pool.join()

        logging.info("All Docker images completed successfully.")

    except FileNotFoundError:
        logging.error(f"Config file '{config_file}' not found.")
    except json.JSONDecodeError:
        logging.error(f"Invalid JSON in '{config_file}'.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Docker images based on a JSON configuration file.")
    parser.add_argument("config_file", help="Path to the JSON configuration file")

    args = parser.parse_args()
    main(args.config_file)

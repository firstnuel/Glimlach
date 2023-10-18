import argparse
import json
import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def run_docker_image(image_config, output_directory):
    try:
        image_id = image_config.get("id")
        docker_command = image_config.get("docker-command")

        # Run the Docker image
        subprocess.run(docker_command, check=True)

        # Move the output file to the specified output directory
        output_file = docker_command[-1]  # Get the last argument (output file)
        output_file_path = os.path.join(output_directory, output_file)
        os.rename(output_file, output_file_path)

        logging.info(f"{image_id} completed successfully.")
    except Exception as e:
        logging.error(f"Error running {image_id}: {str(e)}")

def main(config_file):
    try:
        with open(config_file, 'r') as f:
            config = json.load(f)

        images = config.get("images", [])
        output_directory = config.get("output-directory")

        for image_config in images:
            run_docker_image(image_config, output_directory)

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

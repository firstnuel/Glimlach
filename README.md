# Glimlach

Glimlach is a cybersecurity automation tool designed to streamline the execution of multiple open-source security tools in a single scan. The project is initiated to support Rauli's research, enabling automated complex security scans with commonly used tools like Nmap, Testssl.sh, and Ssh-audit. This tool is a Python script that allows you to run Docker tools in parallel based on a JSON configuration file. It is designed to make it easy to automate the execution of Docker images with customizable parameters.

The primary objective is to facilitate the execution of various cybersecurity tools as a single scan without the need for individual installations and configurations. Glimlach focuses on the containerized execution (OCI) of tools, allowing for isolation and reproducibility.

## Getting Started

Follow these steps to use Glimlach:

### Prerequisites

- Python 3.x installed on your system.
- Docker installed on your system.

### Installation

Install Glimlach using pip:

```bash
pip install glimlach

```

1. Usage
- Create a configuration file in JSON format. The configuration file specifies the Docker images you want to run, their command-line arguments, and output file paths. The sample file is attached [here.](config.json)

```json
{
    "values": {
        "IP": "<Replace your IP here>",
        "out_dir": "<Path to your output directory>",
        "web": "<URL for the tool input>"
        "if": "<Replace your port ID here>"
    },
    "images": [
        {
            "id": "nmap",
            "cli-args": ["-v", "<out_dir>output:/output", "instrumentisto/nmap", "<ip>", "-oN", "/output/nmap_output.txt"]
        },
        {
            "id": "nitko",
            "cli-args": ["-v", "<out_dir>output:/output", "frapsoft/nikto", "-host", "<web>", "-o", "/output/nikto_output.txt"]
        }
    ]        
    }
```

 Glimach uses a JSON configuration file to specify the Docker containers and their parameters. Here's a breakdown of the configuration structure:

- "values": Define custom values that replace placeholders in Docker command arguments.
- "images": Specify the Docker containers you want to run. Each container has an ID, Docker command arguments, and an optional bandwidth limit.


3. Run the Glimlach script with the  ```run-docker-images ``` your configuration path and file as an argument:

   ```
   run-docker-images path/to/your_config_file.json
   ```

 

5. Replace **path/to/your_config_file.json** with the path and name of your configuration file.

- Glimlach will execute the Docker images specified in your configuration, passing the provided command-line arguments, and save the output files in the specified output directory.

### License:

This project is licensed under the MIT License; see the [LICENSE](https://github.com/firstnuel/Glimlach/blob/main/License) file for details.

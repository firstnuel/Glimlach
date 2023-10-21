# Glimlach

Glimach is a Python script that allows you to run Docker containers in parallel based on a JSON configuration file. It is designed to make it easy to automate the execution of Docker images with customizable parameters.

## Getting Started

Follow these steps to use Glimlach:

### Prerequisites

- Python 3.x installed on your system.
- Docker installed on your system.

### Installation

1. Clone the Glimlach repository to your local machine:

   ```bash
   git clone git@github.com:firstnuel/Glimlach.git
   cd glimlach 

2. Install the required Python packages (make sure you have pip installed):

```bash
pip install -r requirements.txt
```
3. Usage
- Create a configuration file in JSON format. The configuration file specifies the Docker images you want to run, their command-line arguments, and output file paths Here's an example configuration file (docker_config.json):
```
{
    "values": {
        "ip": "192.168.101.1",
        "out_dir": "/Users/ikwunna/Desktop/",
        "web": "https://facebook.com"
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
4. Glimach uses a JSON configuration file to specify the Docker containers and their parameters. Here's a breakdown of the configuration structure:

- "values": Define custom values that replace placeholders in Docker command arguments.
- "images": Specify the Docker containers you want to run. Each container has an ID, Docker command arguments, and an optional bandwidth limit.

- Run the Glimlach script with your configuration file as an argument:

```python cli.py config.json```

5. Replace docker_config.json with the name of your configuration file.

- Glimlach will execute the Docker images specified in your configuration, passing the provided command-line arguments, and save the output files in the specified output directory.

### License:

This project is licensed under the MIT License; see the [LICENSE](https://github.com/firstnuel/Glimlach/blob/main/License) file for details.

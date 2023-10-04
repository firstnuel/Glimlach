# Glimlach

Glimlach is a project that allows you to easily run Docker images based on a configuration file. It simplifies the process of specifying Docker images, their command-line arguments, and output file paths.

## Getting Started

Follow these steps to use Glimlach:

### Prerequisites

- Python 3.x installed on your system.
- Docker installed on your system.

### Installation

1. Clone the Glimlach repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/glimlach.git
   cd glimlach 

2. Install the required Python packages (make sure you have pip installed):

```bash
pip install -r requirements.txt
```
3. Usage
- Create a configuration file in JSON format. The configuration file specifies the Docker images you want to run, their command-line arguments, and output file paths Here's an example configuration file (docker_config.json):
```
{
    "images": [
        {
            "id": "nmap",
            "image-name": ["nmap/nmap"],
            "cli-args": "-oX" "nmap_output.xml" "192.168.101.1",
            "output-file": []"nmap_output.xml"
        },
        {
            "id": "testssl",
            "image-name": ["drwetter/testssl.sh"],
            "cli-args": "--jsonfile" "testssl_output.json" "192.168.101.1",
            "output-file": "testssl_output.json"
        }
    ],
    "output-directory": "/path/to/output/directory/"
}
```
4. Customize the "images" section with your desired Docker images and arguments. Ensure you have the correct Docker image names and tags.

Run the Glimlach script with your configuration file as an argument:

```python docker_cli.py docker_config.json```

5. Replace docker_config.json with the name of your configuration file.

Glimlach will execute the Docker images specified in your configuration, passing the provided command-line arguments, and save the output files in the specified output directory.

License
This project is licensed under the MIT License - see the LICENSE file for details.

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

2. Install the required Python packages (or make sure you have pip installed):

**On Ubuntu OS:**

* To install pip for Python 3 on Ubuntu 20.04 run the following commands as root or sudo user in your terminal:

   ```bash
   sudo apt update && sudo apt upgrade
   ```

* Install the supporting software with the command:

   ```bash
   sudo apt install software-properties-common
   ```

   The software-properties-common package gives you better control over your package manager by letting you add PPA (Personal Package Archive) repositories.

* Add the PPA by entering the following:

  ```bash
  sudo add-apt-repository ppa:deadsnakes/ppa
  ```
   Deadsnakes is a PPA with newer releases than the default Ubuntu repositories.
  
* Refresh the package lists again:

  ```bash
  sudo apt update
  ```

* Install pip for Python 3

  ```bash
  sudo apt install python3-pip
  ```

* When the installation is complete, verify the installation by checking the pip version:

   ```bash
   pip3 --version
   ```

**On CentOS OS:**

* To update system repositories, open a terminal window and enter the following command:

   ```bash
   sudo yum update
   ```
   This will refresh the local list of available software packages.

* Some newer versions of CentOS 8 include Python 3 by default. If the system already has Python 3 installed, skip this step.

  To install Python 3, open a terminal window and enter the command:

  ```bash
  sudo yum –y install python3
  ```

* To install Pip for Python 3 open the terminal window, and enter the following:

  ```bash
  sudo yum –y install python3-pip
  ```
  
* When the installation is complete, verify the installation by checking the pip version:

   ```bash
   pip3 --version
   ```


3. Usage
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

4. Glimach uses a JSON configuration file to specify the Docker containers and their parameters. Here's a breakdown of the configuration structure:

- "values": Define custom values that replace placeholders in Docker command arguments.
- "images": Specify the Docker containers you want to run. Each container has an ID, Docker command arguments, and an optional bandwidth limit.
- Run the Glimlach script with your configuration file as an argument:

   ```py
   python cli.py config.json
   ```
   or 
   ```py
   python3 cli.py config.json
   ```

5. Replace **config.json** with the name of your configuration file.

- Glimlach will execute the Docker images specified in your configuration, passing the provided command-line arguments, and save the output files in the specified output directory.

### License:

This project is licensed under the MIT License; see the [LICENSE](https://github.com/firstnuel/Glimlach/blob/main/License) file for details.

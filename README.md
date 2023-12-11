# Glimlach

Glimlach is a cybersecurity automation tool designed to streamline the execution of multiple open-source security tools in a single scan. The project is initiated to support Rauli's research, enabling automated complex security scans with commonly used tools like Nmap, Testssl.sh, and Ssh-audit. This tool is a Python script that allows you to run Docker tools in parallel based on a JSON configuration file. It is designed to make it easy to automate the execution of Docker images with customizable parameters.

The primary objective is to facilitate the execution of various cybersecurity tools as a single scan without the need for individual installations and configurations. Glimlach focuses on the containerized execution (OCI) of tools, allowing for isolation and reproducibility.

## Features of Glimlach

**Tool Integration:**

Glimlach integrates well-known tools like Nmap, Testssl.sh, and Ssh-audit, making it versatile for comprehensive security assessments. Each tool is run in a container, minimizing dependencies and ensuring consistent execution across different environments.

**Centralized Configuration:**

Configuration for the tools is centralized into a single file or directory, simplifying management and ensuring uniformity in scan parameters.
Command-line arguments, output file/directory names, and scan-specific options are defined in this central configuration.

**Parallel Execution:**

Glimlach enables parallel execution of multiple tools, enhancing efficiency and reducing scan time.
Users can configure the parallelism limit based on their system capabilities.

**Reproducibility and Reliability:**

The tool is designed to handle interruptions or tool failures gracefully.
In case of interruptions, a re-run defaults to starting only the tools that have not completed yet, ensuring reliability and consistency.

**Dependency Management:**

Glimlach does not require the creation of containers, leveraging the availability of numerous pre-existing containers on platforms like Docker Hub.
This design choice minimizes the overhead of container management.

**Results Collection:**

Results from all tools in a scan are collected into a single output directory.
A master output JSON file specifies the location of results for each individual tool, offering a consolidated view of the scan outcomes.

**Flexibility and Extensibility:**

The tool supports the running of a single tool multiple times with different options, providing flexibility for diverse scanning requirements.
It also enables running a tool after another, facilitating sequential execution when results from one tool are needed as input for another.

**Cross-Platform Compatibility:**

Glimlach is designed for Linux, and while support for Windows and other platforms is a bonus, it focuses on the cross-platform nature of cybersecurity needs.

**Open Source Licensing:**

Glimlach is provided with a liberal open-source license, encouraging collaboration, contributions, and widespread adoption within the cybersecurity community.

**Modern Technology Stack:**

Glimlach is implemented in Python 3 with type hints in the source code, aligning with modern development practices.
While Python is the primary language, discussions about using other modern languages like Rust or Go are welcome.

**Ease of Use:**

Glimlach aims to be user-friendly, allowing researchers and cybersecurity professionals to easily orchestrate complex scans with minimal manual intervention.

**Availability and Usage:**

The tool is available for use on platforms with Python 3 and a Docker or equivalent container client installed.
Its simplicity and effectiveness make it a valuable asset in automating and enhancing cybersecurity research and assessments.

Read full Documentation at [Glimlach Documentation]https://firstnuel.github.io/Glimlach/Documentation.html)

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
        "parallel_limit": "<Number of tools>",
        "output_directory": "<Path to your output directory>",
        "completed_images": "<Path to your directory>/completed_images.txt"
    },

    "placeholders": {
        "IP": "<Replace your IP here>",
        "out_dir": "<Path to your output directory>",
        "web": "<URL for the tool input>",
        "if": "<Replace your port ID here>",
        "nmap": "instrumentisto/nmap",
        "nikto": "sullo/nikto",
        "<given image id name>": "<docker image name>"
    },

    "images": [
        {
            "id": "nmap",
            "cli-args": ["-v", "<out_dir>output:/output", "instrumentisto/nmap", "<ip>", "-oN", "/output/nmap_output.txt"]
        },
        {
            "id": "nmap2",
            "cli-args": ["-v", "<output_directory>/output:/output", "<nmap>", "-sX", "-T4", "<ip>", "-oN", "output/nmap_output2.txt"]
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


3. Run the Glimlach script with the  ```glimlach ```  command coupled with your configuration path and file as an argument:

   ```
   glimlach path/to/your_config_file.json
   ```

 

5. Replace **path/to/your_config_file.json** with the path and name of your configuration file.

- Glimlach will execute the Docker images specified in your configuration, passing the provided command-line arguments, and save the output files in the specified output directory.

### License:

This project is licensed under the MIT License; see the [LICENSE](https://github.com/firstnuel/Glimlach/blob/main/License) file for details.

# Nemo: Comprehensive Network Scanning and Monitoring Tool

![Nemo Banner](https://www.gitkraken.com/wp-content/uploads/2022/02/CLI-stands-forHero.png)

---

## Table of Contents

1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
    - [Ping Sweep](#ping-sweep)
    - [Port Scan](#port-scan)
    - [Advanced Scan](#advanced-scan)
    - [Bandwidth Monitoring](#bandwidth-monitoring)
    - [Latency Measurement](#latency-measurement)
    - [Alert System](#alert-system)
    - [Report Generation](#report-generation)
5. [Architecture](#architecture)
6. [Technologies Used](#technologies-used)
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

---

## Introduction

Nemo is a powerful and user-friendly network scanning and monitoring tool designed for IT professionals, network administrators, and cybersecurity enthusiasts. This project aims to simplify network management tasks by providing a comprehensive suite of tools to scan, monitor, and analyze network performance and security.

## Features

- **Ping Sweep:** Identify active devices on the network by scanning IP ranges.
- **Port Scan:** Detect open ports and services, with detailed service version detection.
- **Advanced Scan:** Perform detailed scans with additional options for service version detection.
- **Bandwidth Monitoring:** Monitor network usage in real-time.
- **Latency Measurement:** Measure latency to various hosts to diagnose network issues.
- **Alert System:** Send alerts based on predefined conditions.
- **Report Generation:** Generate detailed reports for different types of scans and analyses.

## Installation

### Prerequisites

Ensure you have the following installed on your system:

- Python 3.8+
- `pip` (Python package installer)

### Steps

1. Clone the repository:
    ```sh
    git clone https://github.com/kc-clintone/nemo.git
    cd nemo
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Install `python-nmap` (if not already installed):
    ```sh
    sudo apt-get install python-nmap
    ```

## Usage

Run the main script to access Nemo's functionalities:
```sh
nemo <command> [<args>]
```

#### Ping Sweep

Perform a ping sweep to identify active devices on a network.
```sh
nemo p -i <ip-range>
```
Example:
```sh
nemo p -i 192.168.1.0/24
```

#### Port Scan

Perform a port scan on a specified IP address and port range.
```sh
nemo ps -i <ip> -r <range>
```
Example:
```sh
nemo ps -i 127.0.0.1 -r 20-80
```

#### Advanced Scan

Perform a detailed port scan with service version detection.
```sh
nemo a -i <ip> -r <range> -sV
```
Example:
```sh
nemo a -i 127.0.0.1 -r 20-80 -sV
```

#### Bandwidth Monitoring

Monitor bandwidth usage on a specified network interface.
```sh
nemo b -i <interface>
```
Example:
```sh
nemo b -i eth0
```

#### Latency Measurement

Measure latency to a specified host.
```sh
nemo l -H <host>
```
Example:
```sh
nemo l -H google.com
```

#### Alert System

Send an alert with a specified message.
```sh
nemo al -m <message>
```
Example:
```sh
nemo al -m "Network down!"
```

#### Report Generation

Generate a report for a specified scan type.
```sh
nemo r -t <type>
```
Example:
```sh
nemo r -t ping
```

## Architecture

Nemo's architecture consists of several modules that work together to provide comprehensive network scanning and monitoring functionalities. The main components are:

- **Scanners:** Modules for performing ping sweeps, port scans, and advanced scans.
- **Monitors:** Modules for monitoring bandwidth usage and measuring latency.
- **Alerts:** A system for sending alerts based on predefined conditions.
- **Reports:** A system for generating detailed reports based on scan results.

## Technologies Used

- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Python 3.8+
- **Libraries:** `argparse`, `subprocess`, `termcolor`, `pyfiglet`
- **Tools:** `python-nmap` for network scanning

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature
    ```
3. Commit your changes:
    ```sh
    git commit -m 'Add your feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature
    ```
5. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](MIT) file for details.

## Contact

Created by [Kaysee](www.linkedin.com/in/clinton-otieno) - feel free to contact me!

- LinkedIn: [linkedin](www.linkedin.com/in/clinton-otieno)
- GitHub: [github](www.github.com/kc-clintone)
- Twitter: [twitter](www.twitter.com/kc_clintone)

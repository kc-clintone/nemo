# Netmon Network Tool Documentation

Welcome to the documentation for the Network Tool, an advanced network scanning and monitoring CLI tool.

## Contents
- [Usage](usage.md)
- [Installation](installation.md)

# Usage

## Ping Sweep

```bash
network_tool ping 192.168.1.1/24



# Installation

To install the Network Tool, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/kc-clintone/netmon.git
    cd netmon
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv netmon-env
    source netmon-env/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Install the tool:
    ```bash
    python setup.py install
    ```

You can now use the `netmon` CLI command.


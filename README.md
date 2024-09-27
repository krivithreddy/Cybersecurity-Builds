# Cybersecurity Builds Portfolio

Welcome to my Cybersecurity Builds Portfolio. This repository showcases various projects and builds I've worked on in the field of cybersecurity. Each project highlights different skills, including scripting, process management, and system configuration.

## Table of Contents
## Table of Contents
- [Project 1: Python Daemon with Supervisor](#project-1-python-daemon-with-supervisor)
- [Project 2: TCP Stream Aggregator](#project-2-tcp-stream-aggregator)
- [Project 3: Another Project](#project-3-another-project)
- [Project 4: More Projects](#project-4-more-projects)


## Project 1: Python Daemon with Supervisor
- **Description**: A Python script running as a daemon, managed by Supervisor, that logs the current UTC time every 5 seconds.
- **Technologies**: Python, Supervisor, Linux
- **Key Features**: Demonstrates process management and logging.
- **[View Code](./python-daemon/python_daemon.py)**

## Project 2: TCP Stream Aggregator
- **Description**: A Python script that processes TCP streams from a PCAP file and extracts specific data for analysis.
- **Technologies**: Python, Wireshark/TShark, Linux
- **Key Features**: Automates the extraction of TCP stream data, allowing for easier analysis and processing of network traffic. The script iterates over multiple streams and handles both ASCII and binary data.
- **[View Code](./tcp_stream_aggregator/tcp_stream_aggregator.py)**


## Project 3: More Projects
- **Description**: Additional projects and builds.
- **Technologies**: Technologies or tools used.
- **Key Features**: Any highlights or important details.
- **[View Code](./more-projects/path-to-code)**

## Setup Instructions

### To run the Python daemon project:
1. Place the `python_daemon.py` script in `/opt/`.
2. Configure Supervisor with `python_daemon.conf` in `/etc/supervisor/conf.d/`.
3. Reload Supervisor and start the daemon.

### To run the TCP Stream Aggregator project:
1. Ensure that you have Python and TShark installed on your system.
2. Run the `tcp_stream_aggregator.py` script with the required PCAP file as an argument.
3. Example usage: `python3 tcp_stream_aggregator.py /path/to/your.pcap`



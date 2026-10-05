# Network Packet Analyzer

A Python-based network packet analyzer that captures and inspects network traffic to display useful information about IP packets and common network protocols.

This project was created to practice network traffic analysis and understand how devices communicate across a network.

## Features

- Captures live network packets
- Displays source and destination IP addresses
- Identifies TCP, UDP, and ICMP traffic
- Displays source and destination ports for TCP and UDP packets
- Detects non-IP packets
- Runs continuously until the user stops the capture

## How It Works

The program uses the Scapy library to capture network packets.

For each captured packet, the program checks whether it contains an IP layer. If it does, the analyzer extracts the source and destination IP addresses.

It then checks the transport protocol:

- TCP: Displays the source and destination ports
- UDP: Displays the source and destination ports
- ICMP: Identifies the packet as ICMP
- Other IP protocols: Displays the protocol number

This provides a simple introduction to packet inspection and network traffic analysis.

## Project Files

- `packet_analyzer.py` - Main Python packet analyzer
- `requirements.txt` - Python dependency required by the project
- `.gitignore` - Specifies files Git should ignore
- `README.md` - Project documentation

## Requirements

- Python 3
- Scapy
- Administrator/root privileges may be required for packet capture

Install the required dependency using:

```bash
pip install -r requirements.txt
```

## How to Run

Run the program from a terminal:

```bash
python3 packet_analyzer.py
```

If packet capture requires additional permissions on Linux or macOS, run:

```bash
sudo python3 packet_analyzer.py
```

Press `Ctrl+C` to stop capturing packets.

## Example Output

```text
============================================================
Source IP: 192.168.1.10
Destination IP: 8.8.8.8
Protocol: UDP
Source Port: 54321
Destination Port: 53
```

The IP addresses and ports shown will depend on the network traffic being captured.

## Security & Ethical Use

This project is intended for educational purposes and authorized network analysis only.

Only capture or analyze network traffic on systems and networks that you own or have explicit permission to monitor.

## Skills Demonstrated

- Python
- Network traffic analysis
- Packet inspection
- TCP/IP fundamentals
- TCP, UDP, and ICMP protocols
- IP address analysis
- Port analysis
- Scapy
- Basic network security concepts

## Author

**Mohamed Kordi**
Cybersecurity Engineering Student
University of Sharjah

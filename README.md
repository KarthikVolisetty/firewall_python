**Simple Firewall using Python**

**Project Description**

This project implements a simple firewall using Python, which filters and monitors incoming network traffic based on predefined rules such as IP addresses and ports. The firewall inspects incoming packets and either allows or blocks them, providing a basic layer of network security.

**Features:**

IP-based filtering: Blocks or allows traffic from specific IP addresses.

Port-based filtering: Blocks or allows traffic on specific ports.

Logging: Displays whether packets are allowed or blocked based on the rules.

Custom traffic generation: Traffic can be simulated from specific IP addresses to test the firewall.


**Prerequisites**

**To run the firewall, you need the following:**

  Python 3.x installed on your system.
  Scapy Python library for generating and inspecting network traffic.

**Install Scapy using:**

  pip install scapy

**Installation**

1. Clone this repository:

	git clone https://github.com/your-username/firewall_python.git

2. Navigate to the project directory:

	cd firewall_python

3. Run the firewall script using Python:

	sudo python firewall_python.py

Note: The script needs to be executed with sudo or elevated privileges to monitor and manipulate network traffic.

**How to Use**

1. Run the firewall:

The firewall will automatically start listening for incoming traffic and apply the predefined filtering rules.
The rules can be customized in the code by modifying the block_ip, allow_ip, block_port, and allow_port variables.

2. Simulate traffic: 
You can use tools like Scapy, netcat, or ping to simulate traffic for testing the firewall.

**Testing**
To test the firewall functionality, use the following tools:

	Ping: To test ICMP packets.
	Netcat (nc): To test TCP/UDP connections on specific ports.
	Scapy: For custom traffic generation.
You can create your own test cases based on the IP addresses and port numbers you want to block or allow.

Example Test:
1. Block traffic from IP 192.168.1.10:
	Set block_ip = "192.168.1.10" in the script.
	Simulate traffic from that IP using Scapy.
2. Allow traffic on port 80 (HTTP):
	Set allow_port = 80.
	Test using netcat:
		nc -zv 192.168.1.1 80
		
**Limitations**
	This is a basic firewall implementation for educational purposes.
	It is not designed for production use.
	Advanced traffic filtering, stateful inspection, and protocol handling are not supported in this version.

**Future Enhancements**
	Add support for outbound traffic filtering.
	Improve logging and reporting of traffic statistics.
	Implement stateful packet inspection (tracking connections).
	Add support for more protocols (e.g., UDP filtering).

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

**Acknowledgments**
	The Scapy library was used for packet crafting and inspection.
	Basic network concepts and inspiration for firewall development were taken from various Python networking tutorials.

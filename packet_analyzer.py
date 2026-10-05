from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
print("\n" + "=" * 60)

# Check if the packet contains an IP layer
if IP in packet:
source_ip = packet[IP].src
destination_ip = packet[IP].dst

print(f"Source IP: {source_ip}")
print(f"Destination IP: {destination_ip}")

# Check for TCP traffic
if TCP in packet:
print("Protocol: TCP")
print(f"Source Port: {packet[TCP].sport}")
print(f"Destination Port: {packet[TCP].dport}")

# Check for UDP traffic
elif UDP in packet:
print("Protocol: UDP")
print(f"Source Port: {packet[UDP].sport}")
print(f"Destination Port: {packet[UDP].dport}")

# Check for ICMP traffic
elif ICMP in packet:
print("Protocol: ICMP")

else:
print(f"Protocol Number: {packet[IP].proto}")

else:
print("Non-IP packet detected.")


def main():
print("Network Packet Analyzer")
print("Capturing packets... Press Ctrl+C to stop.\n")

try:
sniff(prn=analyze_packet, store=False)
except KeyboardInterrupt:
print("\nPacket capture stopped.")
except PermissionError:
print("\nPermission denied. Try running the program with administrator/root privileges.")


if __name__ == "__main__":
main()

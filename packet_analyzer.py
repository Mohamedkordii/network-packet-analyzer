from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    print("\n" + "=" * 60)

    if IP in packet:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")

        if TCP in packet:
            print("Protocol: TCP")
            print(f"Source Port: {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol: UDP")
            print(f"Source Port: {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol: ICMP")

        else:
            print(f"Protocol Number: {packet[IP].proto}")

def main():
    print("Network Packet Analyzer")
    print("Capturing packets... Press Ctrl+C to stop.\n")
    sniff(prn=analyze_packet, store=False, count=10)

if __name__ == "__main__":
    main()

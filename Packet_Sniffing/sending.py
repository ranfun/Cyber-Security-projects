from scapy.all import *

def send_packets():
    dst_ip = "192.168.137.77"  # Replace with your machine's IP address
    src_ips = [f"192.168.86.{i}" for i in range(1, 11)]  # Replace with appropriate IP range
    dst_ports = range(1024, 1034)  # Destination port range

    for src_ip, dst_port in zip(src_ips, dst_ports):
        packet = IP(src=src_ip, dst=dst_ip) / TCP(sport=RandShort(), dport=dst_port)
        send(packet)

if __name__ == "__main__":
    send_packets()
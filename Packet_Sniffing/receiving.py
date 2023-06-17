from scapy.all import *

def receive_packets():
    filter_expr = "(tcp and (src host 192.168.137.1 or src host 192.168.137.2 or src host 192.168.137.3 or src host 192.168.137.4 or src host 192.168.137.5 or src host 192.168.137.6 or src host 192.168.137.7 or src host 192.168.137.8 or src host 192.168.137.9 or src host 192.168.137.10)) and (dst portrange 1024-1033)"
    packets = sniff(filter=filter_expr, prn=print_packet_summary, timeout=10)

def print_packet_summary(packet):
    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    src_port = packet[TCP].sport
    dst_port = packet[TCP].dport
    print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Source Port: {src_port}, Destination Port: {dst_port}")

if __name__ == "__main__":
    receive_packets()
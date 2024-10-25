import scapy

def pHandler(packet):
  if packet.haslayer(ICMP) and packet[ICMP].type == 8:
    print("Received ICMP request packet:")
    packet.show()

def start_sniffing():
  print("Listening for ICMP packets...")
  sniff(filter="icmp", prn=pHandler, store=0)

if __name__ == "__main__":
    start_sniffing()

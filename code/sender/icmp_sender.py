import scapy

def send_ICMP_request(target_ip):
  packet = IP(dst=target, ttl=1) / ICMP()

  send(packet)

if __name__ == "__main__":
    target = "172.18.0.3"
    send_ICMP_request(target)

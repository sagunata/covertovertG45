from scapy.all import IP, ICMP, send 

def send_ICMP_request(target_ip):
  packet = IP(dst=target, ttl=1) / ICMP()
  send(packet)
  print(f"ICMP request sent to {target} with TTL=1")

if __name__ == "__main__":
    target = "172.18.0.3"
    send_ICMP_request(target)

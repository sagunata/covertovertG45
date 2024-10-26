from scapy.all import IP, ICMP, send 

def send_ICMP_request(target_ip="receiver"):
  packet = IP(dst=target_ip, ttl=1) / ICMP()
  send(packet)
  print(f"ICMP request sent to {target_ip} with TTL=1")

if __name__ == "__main__":
  send_ICMP_request()
  
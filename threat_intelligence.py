import requests

def query_threat_intelligence(ip_address):
    # Query threat intelligence API
    response = requests.get(f"https://api.threatintelligenceplatform.com/v1/ip/{ip_address}")
    data = response.json()
    if data['is_threat'] == True:
        print("Threat intelligence alert:", ip_address)

# Modify packet_handler to include threat intelligence integration
def packet_handler(packet):
    # Extract source IP address from packet
    src_ip = packet[IP].src
    query_threat_intelligence(src_ip)
    print(packet.summary())

# Start capturing packets
sniff(prn=packet_handler, store=0)

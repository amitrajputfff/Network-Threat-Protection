import re

def detect_sql_injection(packet):
    payload = str(packet.payload)
    if re.search(r"SELECT\s+\*\s+FROM\s+users\s+WHERE\s+username\s*=\s*'", payload, re.IGNORECASE):
        print("SQL Injection detected:", packet.summary())

# Modify packet_handler to include intrusion detection
def packet_handler(packet):
    detect_sql_injection(packet)
    print(packet.summary())

# Start capturing packets
sniff(prn=packet_handler, store=0)

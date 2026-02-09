import socket

# The target can be an IP address or a domain name
target = "127.0.0.1" 

# Defining a range of ports to scan (e.g., common ports 20-1024)
def port_scan(target):
    print(f"Starting scan on host: {target}")
    
    for port in range(20, 101):
        # Create a new socket object using the AF_INET (IPv4) and SOCK_STREAM (TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout so the script doesn't hang on closed ports
        s.settimeout(0.5)
        
        # connect_ex returns an error code instead of raising an exception
        result = s.connect_ex((target, port))
        
        if result == 0:
            print(f"Port {port}: OPEN")
        
        s.close()

if __name__ == "__main__":
    port_scan(target)

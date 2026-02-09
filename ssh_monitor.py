import time
import os

# Path to the authentication log on most Linux systems (Kali/Ubuntu/Debian)
LOG_FILE = "/var/log/auth.log"

def monitor_ssh():
    print(f"--- Monitoring {LOG_FILE} for failed login attempts ---")
    
    # Check if the file exists before starting
    if not os.path.exists(LOG_FILE):
        print(f"Error: {LOG_FILE} not found. Are you running this on Linux?")
        return

    # Open the file and move to the end so we only see NEW logs
    with open(LOG_FILE, "r") as f:
        f.seek(0, os.SEEK_END)
        
        while True:
            line = f.readline()
            if not line:
                time.sleep(0.1) # Wait briefly for new lines
                continue
            
            # Look for the specific failure string
            if "Failed password" in line:
                # Extracting parts of the log for a cleaner alert
                parts = line.split()
                timestamp = " ".join(parts[:3])
                ip_address = parts[-4] # Usually the 4th item from the end
                user = parts[-6]       # The username attempted
                
                print(f"[!] ALERT: Failed login for '{user}' from {ip_address} at {timestamp}")

if __name__ == "__main__":
    try:
        monitor_ssh()
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

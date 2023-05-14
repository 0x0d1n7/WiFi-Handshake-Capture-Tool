WiFi Handshake Capture Tool

This Python script automates the usage of airmon-ng, airodump-ng, and aireplay-ng tools to capture WiFi handshakes. It simplifies the process of enabling monitor mode, scanning for wireless networks, performing a deauthentication attack, and saving the captured handshake file.
Features

    Enables monitor mode on a wireless interface using airmon-ng
    Scans for available wireless networks using airodump-ng
    Performs a deauthentication attack using aireplay-ng to capture the handshake
    Allows customization of output file name and location

Prerequisites

    Python 3
    airmon-ng, airodump-ng, and aireplay-ng tools installed

Usage

    Clone the repository and navigate to the project directory.
    Run the script using Python 3:

    python3 wifi_automation.py

    Follow the prompts to enter the wireless interface, output directory, and handshake file name.
    The script will enable monitor mode, scan for wireless networks, perform a deauthentication attack, and save the captured handshake file.


Disclaimer

This script is intended for educational and ethical purposes only. It is your responsibility to ensure that you have proper authorization to capture WiFi handshakes. Please comply with all applicable laws and regulations.
License

This project is licensed under the MIT License.

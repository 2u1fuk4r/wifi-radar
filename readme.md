![giphy (2)](https://github.com/2u1fuk4r/wifi-radar/assets/48758393/1a18f2ac-601a-4f69-916b-b65e9cc32e88)
# WiFi Security Monitor

This tool is used to monitor your WiFi network and detect death attacks. Intrusion detection changes detect the attacker's MAC address and attack components.

![wifi-radar](https://github.com/2u1fuk4r/wifi-radar/assets/48758393/500f3bbc-814c-4573-adbd-de1ac8e6cf7a)

## Requirements

- Python 3
- pip 
- Scapy
- Tkinter

## Install

You can install the necessary dependencies by following the steps below:

1. `install.sh` run the script:

    ```bash
    chmod +x install.sh
    ./install.sh
    ```


2. The above commands will install all required packages and dependencies.

## Use

Once the installation is complete, you can use the following command to launch the tool:
Your wifi card must be in listening mode.

```bash
ifconfig wlan0 down
iwconfig wlan0 mode monitor
ifconfig wlan0 up

```bash
python3 wifi-radar.py

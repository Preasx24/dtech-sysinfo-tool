#!/bin/bash

# Clear the screen
clear

# D-TECH Branding
figlet "D-TECH SYS INFO"
echo "Tool by D-TECH (Powered by PREASX24)"
echo "-----------------------------------"
echo "Date: $(date)"
echo "Uptime: $(uptime -p)"
echo "Memory Usage:"
free -h
echo "-----------------------------------"
echo "Storage Usage:"
df -h | grep /data
echo "-----------------------------------"
echo "Battery Info:"
termux-battery-status
echo "-----------------------------------"
echo "IP Address: $(curl ifconfig.me)"
echo "-----------------------------------"
echo "Network Info:"
termux-wifi-connectioninfo
echo "-----------------------------------"
echo "More system info:"
neofetch
echo "-----------------------------------"
echo "D-TECH: Stay tuned for more tools!"

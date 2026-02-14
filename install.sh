#!/bin/bash

# Must be root
if [ "$EUID" -ne 0 ]; then
    echo "This installer must be run as rootsudo ./install.sh
    exit 1
fi

# Install the script
cp fan_setup.py /usr/bin/gpio_fan_setup
chmod +x /usr/bin/gpio_fan_setup

echo "Installed gpio_fan_setup to /usr/bin"

#!/bin/bash
sudo apt-get update
sudo apt install vim
pip3 install RPi.GPIO
pip3 install datetime
sudo apt-get install mpg321
sudo echo "python3 /home/pi/daily_audio/main.py &" >> ~/.bashrc
echo "Setup is complete. Device will reboot in 3 seconds."
sleep 3
sudo reboot

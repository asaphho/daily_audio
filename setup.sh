#!/bin/bash
sudo apt-get update
sudo apt install vim
pip3 install RPi.GPIO
pip3 install datetime
sudo apt-get install mpg321

echo "Enter URL to download audio files from (Do NOT include trailing slash):"
read curl_url
sudo sed -i '/export CURL_URL/d' /home/pi/.bashrc
sudo echo "export CURL_URL=$curl_url" >> /home/pi/.bashrc

sudo sed -i '/main.py/d' /home/pi/.bashrc
sudo echo "python3 /home/pi/daily_audio/main.py &" >> /home/pi/.bashrc

echo "Setup is complete. Device will reboot in 3 seconds."
sleep 3
sudo reboot

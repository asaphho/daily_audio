#!/bin/bash
sudo apt-get update
sudo apt install vim
pip3 install RPi.GPIO
pip3 install datetime
sudo apt-get install mpg321
if [[ $(cat /home/pi/.bashrc) != */daily_audio/main.py* ]]
then
sudo echo "python3 /home/pi/daily_audio/main.py &" >> /home/pi/.bashrc
fi
echo "Check every day for corresponding file and download automatically? [y/n]"
while true
do
read curl_prompt
if [[ $curl_prompt == y ]]
  then
  sudo sed -i '/export CURL/d' /home/pi/.bashrc
  sudo echo "export CURL=y" >> /home/pi/.bashrc
  echo "Enter URL (Do NOT include trailing slash):"
  read curl_url
  sudo sed -i '/export CURL_URL/d' /home/pi/.bashrc
  sudo echo "export CURL_URL=$curl_url" >> /home/pi/.bashrc
  break
elif [[ $curl_prompt == n ]]
  then
  sudo sed -i '/export CURL/d' /home/pi/.bashrc
  sudo echo "export CURL=n" >> /home/pi/.bashrc
  break
else
  echo "Please enter 'y' or 'n'."
fi
done
echo "Setup is complete. Device will reboot in 3 seconds."
sleep 3
sudo reboot

#!/bin/bash
if [[ $CURL == y ]]
then
  cd /home/pi/Downloads
  curl --output $(python3 /home/pi/daily_audio/print_filename.py) $CURL_URL/sample2.mp3
  cd /home/pi
fi
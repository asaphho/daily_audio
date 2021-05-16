#!/bin/bash
if [[ $CURL == y ]]
then
  cd /home/pi/Downloads
  filename=$(date +'%Y-%m-%d').mp3
  curl --output $filename $CURL_URL/$filename
  cd /home/pi
fi
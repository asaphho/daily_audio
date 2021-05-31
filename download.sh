#!/bin/bash
if [[ $CURL == y ]]
then
  filename=$(date +'%Y-%m-%d').mp3
  curl --output $HOME/Downloads/$filename $CURL_URL/$filename
fi
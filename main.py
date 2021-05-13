import RPi.GPIO as GPIO
from datetime import datetime
import os
from mutagen.mp3 import MP3

INPUT_PIN = 37

date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
path_to_file = f'/home/pi/Downloads/{date_str}.mp3'
audio_file = MP3(path_to_file)
length_in_seconds = int(audio_file.info.length)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=1000*length_in_seconds)

while True:
    if GPIO.event_detected(INPUT_PIN):
        os.system(f'mpg321 {path_to_file}')

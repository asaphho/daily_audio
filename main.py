import RPi.GPIO as GPIO
from datetime import datetime
import os
from time import sleep
from mutagen.mp3 import MP3

INPUT_PIN = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=5000)

PLAYING = False

while True:
    if GPIO.event_detected(INPUT_PIN) and not PLAYING:
        PLAYING = True
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        path_to_file = f'/home/pi/Downloads/{date_str}.mp3'
        os.system(f'mpg321 {path_to_file}')
        audio_file = MP3(path_to_file)
        length_in_seconds = int(audio_file.info.length)
        sleep(length_in_seconds)
        PLAYING = False

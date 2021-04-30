import RPi.GPIO as GPIO
from datetime import datetime
import os
from time import sleep

PLAYING = False
SLEEP_TIME = 30
INPUT_PIN = 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=5000)

while True:
    if GPIO.event_detected(INPUT_PIN) and not PLAYING:
        PLAYING = True
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        os.system(f'mpg321 /home/pi/Downloads/{date_str}.mp3')
        sleep(SLEEP_TIME)
        PLAYING = False

GPIO.cleanup()

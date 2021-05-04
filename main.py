import RPi.GPIO as GPIO
from datetime import datetime
import os
from time import sleep

INPUT_PIN = 37
SLEEP_TIME = 30

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=5000)

while True:
    if GPIO.event_detected(INPUT_PIN):
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        os.system(f'mpg321 /home/pi/Downloads/{date_str}.mp3')
        GPIO.remove_event_detect(INPUT_PIN)
        sleep(SLEEP_TIME)
        GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=5000)


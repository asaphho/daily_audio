import RPi.GPIO as GPIO
from datetime import datetime
import os

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

GPIO.add_event_detect(10, GPIO.RISING, bouncetime=5000)

while True:
    if GPIO.event_detected(10):
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        os.system(f'mpg321 ~/Downloads/{date_str}.mp3')

GPIO.cleanup()

import RPi.GPIO as GPIO
from datetime import datetime
import os
from time import sleep

INPUT_PIN = 10
SLEEP_TIME = 30

def start_detecting(input_pin):
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(input_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.add_event_detect(input_pin, GPIO.RISING, bouncetime=5000)

while True:
    if GPIO.event_detected(INPUT_PIN):
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        os.system(f'mpg321 /home/pi/Downloads/{date_str}.mp3')
        GPIO.cleanup()
        sleep(SLEEP_TIME)
        start_detecting(INPUT_PIN)


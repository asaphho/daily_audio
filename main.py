import RPi.GPIO as GPIO
from datetime import datetime
import os

INPUT_PIN = 37

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(INPUT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(INPUT_PIN, GPIO.RISING, bouncetime=10000)
os.system('mpg321 /home/pi/daily_audio/fixtures/ready.mp3')

while True:
    if GPIO.event_detected(INPUT_PIN): 
        date_str = datetime.strftime(datetime.now(), '%Y-%m-%d')
        path_to_file = f'/home/pi/Downloads/{date_str}.mp3'
        os.system(f'mpg321 {path_to_file}')

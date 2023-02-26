from time import sleep
import RPi.GPIO as GPIO
from picamera import PiCamera
import Adafruit_DHT


def get_info():
    sensor = Adafruit_DHT.DHT22
    pin = 4
    h,t = Adafruit_DHT.read_retry(sensor, pin)
    return t,h

def water(time):
    GPIO.setwarnings(False) 
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(11,GPIO.OUT)
    GPIO.output(11,True)
    sleep(time*60)
    GPIO.output(11,False)

def make_photo():
    camera = PiCamera()
    camera.capture('./photo.jpg')
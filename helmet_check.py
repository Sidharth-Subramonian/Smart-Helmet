import RPi.GPIO as GPIO
import time

# GPIO setup for ultrasonic sensor
TRIG_PIN = 23
ECHO_PIN = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG_PIN, GPIO.OUT)
GPIO.setup(ECHO_PIN, GPIO.IN)

def is_helmet_worn():
    # Send pulse to trigger the ultrasonic sensor
    GPIO.output(TRIG_PIN, GPIO.LOW)
    time.sleep(0.1)
    GPIO.output(TRIG_PIN, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(TRIG_PIN, GPIO.LOW)

    # Measure the time taken for the pulse to return
    while GPIO.input(ECHO_PIN) == GPIO.LOW:
        pulse_start = time.time()

    while GPIO.input(ECHO_PIN) == GPIO.HIGH:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150

    print(f"[Helmet Check] Distance: {distance:.2f} cm")

    # Assuming the helmet is worn if the distance is above a certain threshold (e.g., more than 1000 cm)
    return distance > 1000

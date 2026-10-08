import time
import requests
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

print("Alert button monitoring system is now active. Press Ctrl+C to stop.")

button_pressed = False
try:
    while True:
        if GPIO.input(7) == GPIO.HIGH and not button_pressed
            requests.post(https://api.telegram.org/bot8689797815:AAHr3n6AjI4aAbktz9F0hiwDpsCy5PdPU5w/sendMessage, json={
    "chat_id": "6567316346",
    "text": "Someone pressed the alert button!
}
            print("Someone pressed the alert button!")
            button_pressed = True
        elif GPIO.input(7) == GPIO.LOW:
            button_pressed = False
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nMonitoring stopped.")
    GPIO.cleanup()

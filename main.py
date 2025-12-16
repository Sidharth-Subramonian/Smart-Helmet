from crash_detection import detect_crash_with_timer
from helmet_check import is_helmet_worn
import time
import telegram
from telegram import Bot

# Initialize Telegram Bot with your TOKEN and CHAT_ID
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHAT_ID = "YOUR_CHAT_ID"
bot = Bot(token=BOT_TOKEN)

def send_telegram_message(message):
    bot.sendMessage(chat_id=CHAT_ID, text=message)

print("[Smart Helmet] System initialized...")

try:
    while True:
        if is_helmet_worn():
            print("[Status] Helmet is worn.")
            
            if detect_crash_with_timer():
                send_telegram_message("Crash detected! Rider is unresponsive.")
                print("[ALERT] Crash detected! Rider is unresponsive.")
                break
            else:
                print("[Status] No crash.")
        else:
            print("[Status] Helmet is NOT worn.")

        time.sleep(1)

except KeyboardInterrupt:
    print("[Shutdown] Interrupted by user.")

finally:
    import RPi.GPIO as GPIO
    GPIO.cleanup()
    print("[Cleanup] GPIO pins reset.")

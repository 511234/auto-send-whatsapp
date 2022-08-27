import keyboard
import time
from urllib.parse import quote
from webbrowser import open
import pyautogui

receiver = "+85212345678"
message = "Hi34567"


def main():

    try:
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
        time.sleep(7)
        print("After sleeping for 7 seconds")
        pyautogui.press("enter")

    except Exception as e:
        print("not working")
        print(e)


main()

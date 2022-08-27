import time
from urllib.parse import quote
from webbrowser import open
import pyautogui
from dotenv import dotenv_values

config = dotenv_values(".env")
receiver = "+85212345678"
message = "Hi34567"
WIDTH, HEIGHT = pyautogui.size()


def main():
    for key, value in config.items():
        print(key, value)
    try:
        open(
            "https://web.whatsapp.com/send?phone="
            + receiver
            + "&text="
            + quote(message)
        )
        time.sleep(5)
        print("After sleeping for 5 seconds")
        pyautogui.click(WIDTH * 0.65, HEIGHT * 0.6)
        print(pyautogui.position())
        pyautogui.press("enter")

    except Exception as e:
        print("not working")
        print(e)


main()

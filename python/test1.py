import keyboard
import time
from urllib.parse import quote
from webbrowser import open
from pyautogui import click, hotkey, position, size, typewrite


receiver = "+85262304667"
message = "Hi34567"
WIDTH, HEIGHT = size()


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
        click(WIDTH / 2, HEIGHT / 2)
        print(position())
        keyboard.press_and_release("enter")
        # time.sleep(5)
        # print("After sleeping for 5 seconds")
        # for char in message:
        #     if char == "\n":
        #         hotkey("shift", "enter")
        #     else:
        #         typewrite(char)
        # print("Finish typing the message")
        time.sleep(3)

        print("After sleeping for 3 seconds")

    except:
        print("not working")


main()

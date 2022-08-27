import re
import time
from urllib.parse import quote
from operator import itemgetter
from webbrowser import open

import pyautogui

from helper.check_config import check_config

receiver = "+85212345678"
message = "Hi34567"
WIDTH, HEIGHT = pyautogui.size()


def main():
    try:
        sheet_name, raw_url = {**check_config()}.values()
        print("main")
        print(sheet_name, raw_url)
        sheet_url = re.search(r"\/d\/(.*?)\/", raw_url).group(1)
        print(sheet_url)
        
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

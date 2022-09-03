import logging
import math
import os
import pandas
import platform
import sys

from pyvirtualdisplay.display import Display

disp = Display(visible=True, size=(1366, 768), backend="xvfb", use_xauth=True)
disp.start()
import Xlib.display
import pyautogui

if sys.platform == "darwin":
    pyautogui._pyautogui_osx._display = Xlib.display.Display(os.environ["DISPLAY"])
elif platform.system() == "Linux":
    pyautogui._pyautogui_x11._display = Xlib.display.Display(os.environ["DISPLAY"])

import time

from webbrowser import open
from urllib.parse import quote

from helper.variable_getter import get_message, get_name, get_phone
from helper.sanitizer import sanitize_url, sanitize_phone


def send(sheet_name, url):
    try:
        sanitized_url = sanitize_url(sheet_name, url)

        raw_list = pandas.read_csv(sanitized_url, encoding="utf-8").to_dict("records")
        whatsapp_list = [
            {**raw_people, "phone": str(int(raw_people.get("phone")))}
            for raw_people in raw_list
            if raw_people.get("phone") and not math.isnan(raw_people.get("phone"))
        ]

        for whatsapp_receiver in whatsapp_list:
            message = get_message(whatsapp_receiver) or "default message"
            name = get_name(whatsapp_receiver)
            print(f"Going to whatsapp {name}...")
            phone = sanitize_phone(get_phone(whatsapp_receiver))
            open(f"https://web.whatsapp.com/send?phone={phone}&text={quote(message)}")
            print("Before sending message...")
            time.sleep(5)
            pyautogui.press("enter")
            time.sleep(5)
            print("Wait for a few seconds before sending to another person...")
    except Exception as e:
        print("not working, please find your best friend")
        print(e)

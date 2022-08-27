import json
import math
import pandas
import time
from operator import itemgetter
from webbrowser import open
from urllib.parse import quote

import pyautogui

from helper.check_config import check_config
from helper.sanitizer import sanitize_url, sanitize_phone

WIDTH, HEIGHT = pyautogui.size()
config_keys = ("column_names", "sheet_name", "url")


def main():
    try:
        column_names, sheet_name, url = {**check_config()}.values()
        sanitized_url = sanitize_url(sheet_name, url)
        column_names_list = json.loads(column_names)
        print(column_names_list)
        print(type(column_names_list))

        raw_list = pandas.read_csv(sanitized_url).to_dict("records")
        print(raw_list)
        whatsapp_list = [
            {**raw_people, "phone": str(int(raw_people.get("phone")))}
            for raw_people in raw_list
            if raw_people.get("phone") and not math.isnan(raw_people.get("phone"))
        ]
        print("whatsapp_list")
        print(whatsapp_list)

        message = "lulu testing auto whatsapp"
        for whatsapp_receiver in whatsapp_list:
            name = whatsapp_receiver.get("name")
            print(f"Going to whatsapp {name}...")
            phone = sanitize_phone(whatsapp_receiver.get("phone"))
            open(f"https://web.whatsapp.com/send?phone={phone}&text={quote(message)}")
            print("Before sending message...")
            time.sleep(5)
            pyautogui.click(WIDTH * 0.65, HEIGHT * 0.6)
            pyautogui.press("enter")
            time.sleep(5)
            print("Wait for a few seconds before sending to another person...")
    except Exception as e:
        print("not working")
        print(e)


main()

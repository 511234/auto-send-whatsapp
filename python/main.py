import json
import math
import pandas
import time
from operator import itemgetter
from webbrowser import open

import pyautogui

from helper.check_config import check_config
from helper.sanitize_url import sanitize_url

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

        return
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

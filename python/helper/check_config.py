import json
import os
import re
from dotenv import dotenv_values
from typing import Dict

config = dotenv_values(".env")


def check_config() -> Dict[str, str]:
    return {key: value for key, value in config.items()}
    # print("Config in .env: ")
    # for key, value in config.items():
    #     print(key, value)
    # x = {
    #     "column_names": os.environ.get("CUSTOM_GOOGLE_SHEET_COLUMN_NAMES"),
    #     "sheet_name": os.environ.get("CUSTOM_GOOGLE_SHEET_NAME"),
    #     "url": os.environ.get("CUSTOM_GOOGLE_SHEET_URL"),
    # }
    # print(x)
    # return x

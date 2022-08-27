import os
import re
from dotenv import dotenv_values
from typing import Dict

config = dotenv_values(".env")


def check_config() -> Dict[str, str]:
    print("Config in .env: ")
    for key, value in config.items():
        print(key, value)
    return config
    # {
    #     "sheet_name": os.environ.get("CUSTOM_GOOGLE_SHEET_NAME"),
    #     "sheet_url": sheet_url,
    # }

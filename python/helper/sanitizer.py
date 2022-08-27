from re import search
import re
from urllib.parse import quote


def sanitize_phone(phone: str) -> str:
    if re.match("^\+852", phone):
        return phone
    return f"+852{phone}"


def sanitize_url(sheet_name: str, url: str) -> str:
    # Get sheet ID between /d/ and /
    sheet_id = search(r"\/d\/(.*?)\/", url).group(1)
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={quote(sheet_name)}"

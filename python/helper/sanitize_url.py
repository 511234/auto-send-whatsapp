from re import search
from urllib.parse import quote


def sanitize_url(sheet_name: str, url: str):
    # Get sheet ID between /d/ and /
    sheet_id = search(r"\/d\/(.*?)\/", url).group(1)
    return f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={quote(sheet_name)}"

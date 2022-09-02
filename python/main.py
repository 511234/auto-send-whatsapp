from helper.check_config import check_config
from send_whatsapp import send

if __name__ == "__main__":
    _column_names, sheet_name, url = {**check_config()}.values()
    send(sheet_name, url)

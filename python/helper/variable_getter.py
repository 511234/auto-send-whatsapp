def get_name(some_dict: dict) -> str:
    return some_dict.get('name') or some_dict.get('Name') or some_dict.get('姓名')

def get_phone(some_dict: dict)->str:
    return some_dict.get('phone') or some_dict.get('Phone') or some_dict.get('電話')
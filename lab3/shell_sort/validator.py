import re


class Validator:

    def __init__(self):
        pass

    def control_email(email) -> bool:
        if type(email) != str:
            return False
        pattern = '^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$'
        if re.match(pattern, email):
            return True
        return False

    def control_weight(weight: str) -> bool:
        pattern = '\d{2,3}'
        if re.match(pattern, str(weight)) is not None:
            if (int(weight) < 150 and int(weight) > 40):
                return True
        return False

    def control_snils(snils: str) -> bool:
        pattern = '\d{11}'
        if re.match(pattern, str(snils)) is not None:
            return True
        return False

    def control_passport(passport_number: int) -> bool:
        pattern = '\d{6}'
        if re.match(pattern, str(passport_number)) is not None:
            return True
        return False

    def control_address(address) -> bool:
        pattern = '[а-яА-Я \-.0-9]{1,}[а-яА-Я0-9]{1,}'
        if type(address) != str:
            return False
        if re.match(pattern, address):
            return True
        return False

    def control_experience(number) -> bool:
        if type(number) == int:
            if (number < 80 and number > 0):
                return True
        return False

    def control_string(string) -> str:
        if type(string) != str is not None:
            return False
        return True

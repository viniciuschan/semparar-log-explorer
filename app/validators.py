import re
from datetime import datetime


def _is_valid_date(value: str) -> bool:
    cleaned_value = value.replace("-", "").replace("/", "")
    try:
        datetime.strptime(cleaned_value, "%Y%m%d")
        return True
    except ValueError:
        return False


def _is_valid_time(value: str) -> bool:
    cleaned_value = value.replace(":", "")
    try:
        datetime.strptime(cleaned_value, "%H%M%S.%f")
        return True
    except ValueError:
        return False


def _is_valid_code(value: str) -> bool:
    return len(value) == 2 and value.isalnum()


def is_valid_line(date: str, time: str, code: str) -> bool:
    return all(
        [
            _is_valid_date(date) is True,
            _is_valid_time(time) is True,
            _is_valid_code(code) is True,
        ]
    )


def is_valid_tag(value: str) -> bool:
    return len(value) == 10 and value.isdigit()


def _is_valid_plate_old_format(value: str) -> bool:
    pattern = re.compile(r"^[A-Z]{3}[0-9]{4}$")
    return re.match(pattern, value.strip()) is not None


def _is_valid_plate_mercosul_format(value: str) -> bool:
    pattern = re.compile(r"^[A-Z]{3}\d[A-Z]\d{2}$")
    return re.match(pattern, value) is not None


def is_valid_plate(value: str) -> bool:
    cleaned_value = value.upper().strip().replace("-", "")
    return any(
        [
            _is_valid_plate_old_format(cleaned_value),
            _is_valid_plate_mercosul_format(cleaned_value),
        ]
    )


def is_rejection_code(value: str) -> bool:
    _has_valid_chars = value.isdigit() or value in ("!", "*")
    return len(value) <= 2 and _has_valid_chars

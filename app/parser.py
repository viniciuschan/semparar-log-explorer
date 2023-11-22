from app.constants import EVA_ERROR_CODES, PAYMENT_CANCEL_SUB_ERRORS
from app.validators import (
    is_rejection_code,
    is_valid_line,
    is_valid_plate,
    is_valid_tag,
)

MIN_COLUMNS = 3
MAX_COLUMNS = 6


def _get_result_body() -> dict:
    return {
        "date": "",
        "time": "",
        "code": "",
        "tag": "",
        "plate": "",
        "rejection_code": "",
    }


def _add_row_canceled_error_details(row_data: dict) -> dict:
    has_cancel_error = row_data["code"] == "99"
    if has_cancel_error and row_data["rejection_code"] in PAYMENT_CANCEL_SUB_ERRORS:
        row_data[
            "description"
        ] += (
            f" | {PAYMENT_CANCEL_SUB_ERRORS[row_data['rejection_code']]['description']}"
        )
        row_data["action"] = {
            PAYMENT_CANCEL_SUB_ERRORS[row_data["rejection_code"]]["action"]
        }
    return row_data


def _add_row_error_details(row_data: dict) -> dict:
    if row_data["code"] in EVA_ERROR_CODES.keys():
        row_data["description"] = EVA_ERROR_CODES[row_data["code"]]["description"]
        row_data["action"] = EVA_ERROR_CODES[row_data["code"]]["action"]

    row_data = _add_row_canceled_error_details(row_data)
    return row_data


def get_parsed_data(content: list) -> list:
    result = []
    for line in content:
        parsed_data = _get_result_body()
        columns = line.split()

        if len(columns) < MIN_COLUMNS:
            continue

        date = columns[0]
        time = columns[1]
        code = columns[2]

        if not is_valid_line(date, time, code):
            continue

        parsed_data["date"] = date
        parsed_data["time"] = time
        parsed_data["code"] = code

        for idx in range(MIN_COLUMNS, MAX_COLUMNS + 1):
            if len(columns) > idx:
                data = columns[idx]

                if is_valid_plate(data):
                    parsed_data["plate"] = data

                if is_valid_tag(data):
                    parsed_data["tag"] = data

                if is_rejection_code(data):
                    parsed_data["rejection_code"] = data

        detailed_parsed_data = _add_row_error_details(parsed_data)
        result.append(detailed_parsed_data)

    return result

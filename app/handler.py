from app.parser import get_parsed_data

DATA_DIR = "input-data"
RESULT_PATH = "result.txt"


def handle_file(log_path: str, result_path: str = RESULT_PATH) -> bool:
    try:
        with open(log_path, "r") as log_file:
            content = log_file.read().split("\n")
            data = get_parsed_data(content)

            with open(result_path, "a") as result_file:
                for entry in data:
                    result_file.write(f"{entry}\n")
    except Exception as exc:
        print(f"An error occurred while processing {log_path}: {exc}")
        return False

    return True

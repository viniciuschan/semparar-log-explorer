from app.parser import get_parsed_data

DATA_DIR = "input-data"
RESULT_PATH = "result.txt"


def handle_file(log_path: str, result_path: str = RESULT_PATH) -> bool:
    try:
        with open(log_path, "r") as log_file:
            content = log_file.read().split("\n")
            data = get_parsed_data(content)

            with open(result_path, "a") as result_file:
                for idx, entry in enumerate(data):
                    line_number = f"[L-{idx+1}]"
                    line = " ".join(item for item in entry.values())
                    result_file.write(f"{line_number} {line}\n")

    except Exception as exc:
        print(f"An error occurred while processing {log_path}: {exc}")
        return False

    return True

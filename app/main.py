import os

from app.handler import handle_file

DATA_DIR = "input-data"


def process():
    for filename in os.listdir(DATA_DIR):
        file_format = filename.split(".")[-1]
        if file_format in ("log", "txt"):
            log_path = os.path.join(DATA_DIR, filename)
            handle_file(log_path)


if __name__ == "__main__":
    process()

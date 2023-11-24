import os
import tempfile

from app.handler import handle_file


def test_handle_file():
    with tempfile.TemporaryDirectory() as temp_dir:
        result_path = os.path.join(temp_dir, "tmp_result.txt")
        log_path = os.path.join(temp_dir, "tmp_logfile.log")

        with open(log_path, "w") as file:
            file.write("20230711 140613.095 03  GIS6207")

        result = handle_file(log_path, result_path)
        assert result is True
        assert os.path.isfile(result_path) is True

        with open(result_path, "r") as file:
            result_content = file.read().replace("\n", "")
        assert result_content == "[L-1] 20230711 140613.095 03  GIS6207 "

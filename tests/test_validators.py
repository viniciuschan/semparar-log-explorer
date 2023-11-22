import pytest

from app.validators import (
    _is_valid_code,
    _is_valid_date,
    _is_valid_plate_mercosul_format,
    _is_valid_plate_old_format,
    _is_valid_time,
    is_rejection_code,
    is_valid_line,
    is_valid_plate,
    is_valid_tag,
)


@pytest.mark.parametrize(
    "date, expected_result",
    [
        ("20220101", True),
        ("2022-01-01", True),
        ("2022/01/01", True),
        ("invalid", False),
    ],
)
def test_is_valid_date(date, expected_result):
    assert _is_valid_date(date) == expected_result


@pytest.mark.parametrize(
    "time, expected_result",
    [
        ("120304.567", True),
        ("12:03:04.567", True),
        ("12-03-04.567", True),
        ("invalid", False),
    ],
)
def test_is_valid_time(time, expected_result):
    assert _is_valid_time(time) == expected_result


@pytest.mark.parametrize(
    "code, expected_result",
    [
        ("AB", True),
        ("A1", True),
        ("ABC", False),
    ],
)
def test_is_valid_code(code, expected_result):
    assert _is_valid_code(code) == expected_result


@pytest.mark.parametrize(
    "date, time, code, expected_result",
    [
        ("20220101", "120304.567", "AB", True),
        ("invalid", "120304.567", "AB", False),
        ("20220101", "invalid", "AB", False),
        ("20220101", "120304.567", "1AB", False),
    ],
)
def test_is_valid_line(date, time, code, expected_result):
    assert is_valid_line(date, time, code) == expected_result


@pytest.mark.parametrize(
    "tag, expected_result",
    [
        ("1234567890", True),
        ("12345ABCDE", False),
        ("12345678901", False),
        ("invalid", False),
    ],
)
def test_is_valid_tag(tag, expected_result):
    assert is_valid_tag(tag) == expected_result


@pytest.mark.parametrize(
    "plate, expected_result",
    [
        ("ABC1234", True),
        ("XYZ5678", True),
        ("DEF9876", True),
        ("1234ABC", False),
        ("ABCD12345", False),
        ("XYZ@567", False),
        ("AB1C234", False),
    ],
)
def test_is_valid_plate_old_format(plate, expected_result):
    assert _is_valid_plate_old_format(plate) == expected_result


@pytest.mark.parametrize(
    "plate, expected_result",
    [
        ("ABC1D23", True),
        ("1234ABC", False),
        ("ABCD12345", False),
        ("XYZ@567", False),
        ("AB1C234", False),
    ],
)
def test_is_valid_plate_mercosul_format(plate, expected_result):
    assert _is_valid_plate_mercosul_format(plate) == expected_result


@pytest.mark.parametrize(
    "plate, expected_result",
    [
        ("ABC1234", True),
        ("ABC1D23", True),
        ("ABCD123", False),
        ("invalid", False),
    ],
)
def test_is_valid_plate(plate, expected_result):
    assert is_valid_plate(plate) == expected_result


@pytest.mark.parametrize(
    "rejection_code, expected_result",
    [
        ("!", True),
        ("*", True),
        ("AB", False),
        ("", False),
    ],
)
def test_is_rejection_code(rejection_code, expected_result):
    assert is_rejection_code(rejection_code) == expected_result

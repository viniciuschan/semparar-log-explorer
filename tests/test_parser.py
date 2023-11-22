from app.parser import get_parsed_data


def test_get_parsed_data_invalid_line():
    content = ["invalid data"]
    result = get_parsed_data(content)
    assert len(result) == 0
    assert result == []


def test_get_parsed_data_multiple_lines():
    content = [
        "20220101 120304.567 AB",
        "20220102 120305.567 CD",
        "20220103 120306.567 EF",
    ]
    result = get_parsed_data(content)
    assert len(result) == 3
    assert result == [
        {
            "date": "20220101",
            "time": "120304.567",
            "code": "AB",
            "tag": "",
            "plate": "",
            "rejection_code": "",
        },
        {
            "date": "20220102",
            "time": "120305.567",
            "code": "CD",
            "tag": "",
            "plate": "",
            "rejection_code": "",
        },
        {
            "date": "20220103",
            "time": "120306.567",
            "code": "EF",
            "tag": "",
            "plate": "",
            "rejection_code": "",
        },
    ]


def test_get_parsed_data_with_plate_and_tag():
    content = [
        "20220101 120304.567 AB ABC1234 1234567890",
        "20220102 120305.567 CD DEF5678 9876543210",
    ]
    result = get_parsed_data(content)
    assert len(result) == 2
    assert result == [
        {
            "date": "20220101",
            "time": "120304.567",
            "code": "AB",
            "tag": "1234567890",
            "plate": "ABC1234",
            "rejection_code": "",
        },
        {
            "date": "20220102",
            "time": "120305.567",
            "code": "CD",
            "tag": "9876543210",
            "plate": "DEF5678",
            "rejection_code": "",
        },
    ]


def test_get_parsed_data_with_rejection_code():
    content = [
        "20220101 120304.567 AB !",
        "20220101 120304.567 AB *",
        "20220102 120305.567 CD invalid",
    ]
    result = get_parsed_data(content)
    assert len(result) == 3
    assert result == [
        {
            "date": "20220101",
            "time": "120304.567",
            "code": "AB",
            "tag": "",
            "plate": "",
            "rejection_code": "!",
        },
        {
            "date": "20220101",
            "time": "120304.567",
            "code": "AB",
            "tag": "",
            "plate": "",
            "rejection_code": "*",
        },
        {
            "date": "20220102",
            "time": "120305.567",
            "code": "CD",
            "tag": "",
            "plate": "",
            "rejection_code": "",
        },
    ]

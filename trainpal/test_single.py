from single_data import input_data
from trainpal_parser import parser

expected_result = {
    "out": {
        "start": {"station": "Sheffield", "date": "Mon 8 Nov 2021", "time": "08:32"},
        "end": {
            "station": "Manchester Piccadilly",
            "date": "Mon 8 Nov 2021",
            "time": "09:41",
        },
    },
    "rtn": None,
}


def test_result():
    assert parser(input_data) == expected_result


def test_json_encode():
    import json

    blob = parser(input_data)
    json.dumps(blob)


def test_blank_lines():
    body = input_data["body"]
    lines = []
    for line in body.split("\n"):
        lines.append(line)
        lines.append("")
    input_data["body"] = "\n".join(lines)
    assert parser(input_data) == expected_result

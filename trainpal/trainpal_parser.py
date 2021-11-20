"""Plain text Trainpal email parser to extract useful information"""

import re
import datetime


def parser(input_data):
    ## Stations

    subject = input_data["subject"]

    match = re.match(r"Your booking confirmation: ([\w\s]+) - ([\w\s]+)", subject)
    start_station, end_station = match.group(1, 2)

    ## Dates and Times

    body = input_data["body"]

    lines = [line for line in body.split("\n") if line != ""]

    out = lines.index("OUT")

    try:
        rtn = lines.index("RTN")
    except ValueError:
        rtn = -1

    # Parse Outbound
    out_lines = lines[out:rtn]

    out_start_date = out_lines[1]
    out_start_time = out_lines[3]

    # print(f"{out_start_time} {out_start_date} @ {start_station}")

    for line in out_lines[::-1]:
        if re.match(r"\d\d:\d\d", line):
            out_end_time = line
            break
    out_end_date = out_start_date  # TODO: Use day++ if the end time goes beyond midnight - I need to check how this is formatted with an example

    out_blob = {
        "start": {
            "station": start_station,
            "date": out_start_date,
            "time": out_start_time,
        },
        "end": {"station": end_station, "date": out_end_date, "time": out_end_time},
    }

    # print(f"{out_end_time} {out_end_date} @ {end_station}")

    rtn_blob = None

    return {
        "out": out_blob,
        "rtn": rtn_blob,
    }


if __name__ == "__main__":
    from single_data import input_data

    output = parser(input_data)
    print(output)

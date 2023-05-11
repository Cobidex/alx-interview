#!/usr/bin/python3
"""
This script parses log files to extract useful
information such as file size and frequency of HTTP response codes.
"""

import sys
import re


def show_statistics(log_data: dict) -> None:
    """
    Helper function to display statistics
    """
    print("File size: {}".format(log_data["file_size"]))
    for code in sorted(log_data["code_frequency"]):
        if log_data["code_frequency"][code]:
            print("{}: {}".format(code, log_data["code_frequency"][code]))


if __name__ == "__main__":
    regex = re.compile(
    r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - \[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d+\] "GET /projects/260 HTTP/1.1" (.{3}) (\d+)')  # nopep8

    line_count = 0
    log_data = {}
    log_data["file_size"] = 0
    log_data["code_frequency"] = {
        str(code): 0 for code in [
            200, 301, 400, 401, 403, 404, 405, 500]}

    try:
        for line in sys.stdin:
            line = line.strip()
            match = regex.fullmatch(line)
            if match:
                line_count += 1
                code = match.group(1)
                file_size = int(match.group(2))

                # File size
                log_data["file_size"] += file_size

                # status code
                if code.isdecimal():
                    log_data["code_frequency"][code] += 1

                if line_count % 10 == 0:
                    show_statistics(log_data)
    finally:
        show_statistics(log_data)

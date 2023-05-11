#!/usr/bin/python3
"""
Log parsing
"""

import sys
import re
from collections import defaultdict


def display_statistics(log: dict) -> None:
    """
    Display statistics about log file
    """
    print(f"File size: {log['file_size']} bytes")
    for code, count in sorted(log['code_frequency'].items()):
        if count:
            print(f"{code}: {count}")


if __name__ == "__main__":
    # Define regular expression pattern to match log entries
    log_entry_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - '
                                   r'\[(?P<timestamp>.+)\] "(?P<request>.+)" '
                                   r'(?P<status_code>\d{3}) (?P<file_size>\d+)')

    # Initialize variables
    log = defaultdict(int)

    try:
        for line_num, line in enumerate(sys.stdin, start=1):
            line = line.strip()
            match = log_entry_pattern.fullmatch(line)
            if match:
                log["file_size"] += int(match.group('file_size'))

                status_code = match.group('status_code')
                if status_code.isdecimal():
                    log['code_frequency'][status_code] += 1

                if line_num % 10 == 0:
                    display_statistics(log)

        # Display statistics for remaining lines
        display_statistics(log)

    except KeyboardInterrupt:
        # If user presses CTRL+C, print statistics and exit
        display_statistics(log)
        sys.exit(0)

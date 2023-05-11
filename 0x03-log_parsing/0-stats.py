#!/usr/bin/python3
import sys

TOTAL_LINES_TO_PRINT_STATS = 10
status_codes = [200, 301, 400, 401, 403, 404, 405, 500]
status_code_counts = {c: 0 for c in status_codes}
total_file_size = 0
line_count = 0

def print_stats():
    global status_code_counts, total_file_size, line_count
    print("File size: {}".format(total_file_size))
    for c in sorted(status_codes):
        if status_code_counts[c] > 0:
            print("{}: {}".format(c, status_code_counts[c]))
    line_count = 0

try:
    for line in sys.stdin:
        try:
            parts = line.split()
            ip_address = parts[0]
            date_str = parts[3][1:]
            status_code = int(parts[8])
            file_size = int(parts[9])
            total_file_size += file_size
            status_code_counts[status_code] += 1
            line_count += 1
        except:
            pass
        if line_count == TOTAL_LINES_TO_PRINT_STATS:
            print_stats()
except KeyboardInterrupt:
    print_stats()
    sys.exit(0)

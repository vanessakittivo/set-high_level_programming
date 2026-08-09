#!/usr/bin/python3
"""
Read stdin line by line and compute metrics.
"""

import sys


status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_size = 0
line_count = 0


def print_stats():
    """Print the accumulated statistics."""
    print("File size: {}".format(total_size))

    for status in sorted(status_codes):
        if status_codes[status] > 0:
            print("{}: {}".format(status, status_codes[status]))


try:
    for line in sys.stdin:
        parts = line.split()

        if len(parts) < 7:
            continue

        try:
            status = int(parts[-2])
            file_size = int(parts[-1])
        except (ValueError, IndexError):
            continue

        if status in status_codes:
            status_codes[status] += 1

        total_size += file_size
        line_count += 1

        if line_count == 10:
            print_stats()
            line_count = 0

except KeyboardInterrupt:
    print_stats()

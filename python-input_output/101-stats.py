#!/usr/bin/python3
"""Log parsing script."""

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

        try:
            size = int(parts[-1])
            total_size += size
        except (ValueError, IndexError):
            continue

        try:
            status = int(parts[-2])

            if status in status_codes:
                status_codes[status] += 1
        except (ValueError, IndexError):
            pass

        line_count += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
else:
    if line_count % 10 != 0 or line_count == 0:
        print_stats()

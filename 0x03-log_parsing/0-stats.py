#!/usr/bin/python3
""" Log parsing script """
import sys
import signal


# Initialize variables
total_file_size = 0
status_codes_count = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
line_count = 0


def print_stats():
    """ Print the accumulated metrics """
    print("File size: {}".format(total_file_size))
    for code in sorted(status_codes_count.keys()):
        if status_codes_count[code] > 0:
            print("{}: {}".format(code, status_codes_count[code]))


def signal_handler(sig, frame):
    """ Handle keyboard interruption """
    print_stats()
    sys.exit(0)


# Register the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process each line from stdin
for line in sys.stdin:
    line_count += 1
    parts = line.split()

    if len(parts) < 7:
        continue  # Skip malformed lines

    # Extract the status code and file size
    status_code = parts[-2]
    file_size = parts[-1]

    try:
        total_file_size += int(file_size)
        if status_code in status_codes_count:
            status_codes_count[status_code] += 1
    except ValueError:
        continue  # Skip lines with invalid file size

    # Print the metrics every 10 lines
    if line_count % 10 == 0:
        print_stats()

# Print any remaining metrics at the end
print_stats()

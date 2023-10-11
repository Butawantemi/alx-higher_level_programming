#!/usr/bin/python3
import sys
import signal

# Dictionary to store status code counts
status_code_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0,
}

# Variables to keep track of total file size and line count
total_file_size = 0
line_count = 0

def print_statistics():
    """
    Print the computed statistics.
    """
    print("Total file size:", total_file_size)
    sorted_status_codes = sorted(status_code_counts.keys())
    for status_code in sorted_status_codes:
        count = status_code_counts[status_code]
        if count > 0:
            print("{}: {}".format(status_code, count))

def signal_handler(sig, frame):
    """
    Signal handler for CTRL + C (keyboard interruption).
    Print statistics and exit.
    """
    print_statistics()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) >= 10:
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1

        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics()


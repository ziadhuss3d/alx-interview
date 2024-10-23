#!/usr/bin/python3
"""
Log parsing
"""
import sys

def print_metrics(file_size, status_codes):
    """
    Print metrics
    """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))

codes_count = {'200': 0, '301': 0, '400': 0, '401': 0,
               '403': 0, '404': 0, '405': 0, '500': 0}
file_size_total = 0
count = 0

if __name__ == "__main__":
    try:
        for line in sys.stdin:
            try:
                parts = line.split()
                # Get status code and file size
                status_code = parts[-2]
                file_size = int(parts[-1])

                # Update the counts
                if status_code in codes_count:
                    codes_count[status_code] += 1
                file_size_total += file_size
            except Exception:
                pass

            count += 1

            # Print metrics every 10 lines
            if count == 10:
                print_metrics(file_size_total, codes_count)
                count = 0

    except KeyboardInterrupt:
        # Print final metrics after manual interruption
        print_metrics(file_size_total, codes_count)
        sys.exit(0)

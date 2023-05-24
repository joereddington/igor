import sys
import re
from datetime import datetime, timedelta

def find_two_digit_number(line):
    match = re.search(r'\b\d{2}\b', line[:8])
    if match:
        return int(match.group(0))
    return None

def minutes_to_hours_and_minutes(minutes):
    hours, remaining_minutes = divmod(minutes, 60)
    return hours, remaining_minutes

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    total_lines = 0
    lines_with_two_digit_number = 0
    sum_of_minutes = 0

    with open(filename, 'r') as file:
        for line in file:
            total_lines += 1
            number = find_two_digit_number(line)
            if number is not None:
                lines_with_two_digit_number += 1
                sum_of_minutes += number

    print("Total lines:", total_lines)
    print("Lines with a two-digit number in the first eight characters:", lines_with_two_digit_number)

    hours, minutes = minutes_to_hours_and_minutes(sum_of_minutes)
    print(f"total minutes: {sum_of_minutes}")
    print(f"Sum of those numbers (as hours and minutes): {hours} hours, {minutes} minutes")

    current_time = datetime.now()
    print("Current time:", current_time.strftime("%H:%M"))

    new_time = current_time + timedelta(minutes=sum_of_minutes)
    print("Current time plus tasks:", new_time.strftime("%H:%M"))

if __name__ == "__main__":
    main()


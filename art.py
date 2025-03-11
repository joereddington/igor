import csv
import os
import datetime
import argparse

args = {}
here = os.path.dirname(os.path.realpath(__file__))

def setup_argument_list():
    """Creates and parses the argument list for ART (Add recurring tasks)."""
    parser = argparse.ArgumentParser(description="Manages Igor")
    parser.add_argument('-n', action="store_true", help="Show only tasks since the last recorded run")
    parser.set_defaults(verbatim=False)
    return parser.parse_args()

def tasks_since(events, start, end=datetime.date.today().toordinal()):
    return_list = []
    for i in range(start, end):
        return_list.extend(tasks_on_date(events, i))
    return return_list

def tasks_on_date(events, target_date):
    ordinal = target_date if isinstance(target_date, int) else target_date.toordinal()
    return [event[1] for event in events if ordinal % int(event[0]) == 0]

def import_events(filename):
    events = []
    try:
        with open(filename, 'r', newline='') as events_file:
            reader = csv.reader(events_file, skipinitialspace=True)
            for line in reader:
                if line:
                    events.append(line)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    return events

def print_recent_tasks(events, number_of_days_to_go_back=4):
    for i in range(number_of_days_to_go_back + 1):
        day = datetime.date.today() - datetime.timedelta(number_of_days_to_go_back - i)
        print(f"\n{day}")
        for task in tasks_on_date(events, day):
            print(task)

def read_last_date():
    try:
        with open(here + "/art_lastdate.txt") as f:
            return [int(line.strip()) for line in f]
    except FileNotFoundError:
        return [datetime.date.today().toordinal()]

def write_last_date():
    try:
        with open(here + "/art_lastdate.txt", "w") as f:
            f.write(f"{datetime.date.today().toordinal()}")
    except IOError as e:
        print(f"Error writing to file: {e}")

args = setup_argument_list()
events = import_events(here + "/art_events.csv")

if args.n:
    for task in tasks_since(events, read_last_date()[0]):
        print(task)
    write_last_date()
else:
    print("ART V0.1")
    print(f"Current ordinal is: {datetime.date.today().toordinal()}")
    print_recent_tasks(events)


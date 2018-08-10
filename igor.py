import csv

events=[]



def import_events(filename):
    with open(filename, 'rU') as events_file:
        reader = csv.reader(events_file, skipinitialspace=True)
        lines = filter(None, reader)
        for line in lines:
            events.append(line)

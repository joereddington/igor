import csv
import os
import datetime
import argparse

args={}
here= os.path.dirname(os.path.realpath(__file__))

def setup_argument_list():
    "creates and parses the argument list for ART (Add reoccuring tasks)"
    parser = argparse.ArgumentParser( description="manages Igor")
    parser.add_argument('-n', action="store_true", help="Show only tasks since the last recorded run")
    parser.set_defaults(verbatim=False)
    return parser.parse_args()

def tasks_since(events,start,end=datetime.date.today().toordinal()):
    return_list=[]
    for i in range(start,end):
        return_list.extend(tasks_on_date(events,i))
    return return_list
    
def tasks_on_date(events,target_date):
    ordinal=0
    return_list=[]
    if isinstance(target_date,int):
        ordinal=target_date
    else:
        ordinal=target_date.toordinal()
    for event in events:
        if ordinal % int(event[0]) ==0:
            return_list.append(event[1])
    return return_list


def import_events(filename):
    events=[]
    with open(filename, 'rU') as events_file:
        reader = csv.reader(events_file, skipinitialspace=True)
        lines = [_f for _f in reader if _f]
        for line in lines:
            events.append(line)
    return events

def print_recent_tasks(events,number_of_days_to_go_back=4):
    for i in range(number_of_days_to_go_back+1):
        print("")
        print((datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)))
        for task in tasks_on_date(events,datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)):
            print(task)

def read_last_date():
    with open(here+"/art_lastdate.txt") as f:
        return list(map(int, f))

def write_last_date(): #Todo what is an ordinal here
   f=open(here+"/art_lastdate.txt","w")
   f.write("{}".format(datetime.date.today().toordinal()))
   f.close()

def go(): #? Where is this called? 
    events=import_events(here+"/art_events.csv") # Read the events - okay, but then what are they used for? 
    if args.n:
        for task in tasks_since(read_last_date()[0]):
            print(task)
        write_last_date()
    else:
        print("ART V0.1")
        print("Current ordinal is: {}".format(datetime.date.today().toordinal()))
        print_recent_tasks(events)

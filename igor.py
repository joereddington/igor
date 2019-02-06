import csv
import os
import datetime

events=[]


def tasks_since(start,end=datetime.date.today().toordinal()):
    return_list=[]
    for i in range(start,end):
        return_list.extend(tasks_on_date(i))
    return return_list
    


def tasks_on_date(target_date):
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



def generate_list(days,start=0):
    return_list=[]
    for i in range(start,start+days):
        for event in events:
            if i % int(event[0]) ==0:
                return_list.append(event[1])
    return return_list


def import_events(filename):
    with open(filename, 'rU') as events_file:
        reader = csv.reader(events_file, skipinitialspace=True)
        lines = filter(None, reader)
        for line in lines:
            events.append(line)

if __name__=="__main__":

    here= os.path.dirname(os.path.realpath(__file__))
    import_events(here+"/events.csv")
    print "Igor V0.1"
    number_of_days_to_go_back=10
    for i in range(number_of_days_to_go_back+1):
        print ""
        print (datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i))
        for task in tasks_on_date(datetime.date.today()-datetime.timedelta(number_of_days_to_go_back-i)):
            print task

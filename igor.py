import csv
import datetime

events=[]


def tasks_on_date(target_date):
    return_list=[]
    for event in events:
        if target_date.toordinal() % int(event[0]) ==0:
            return_list.append(event[1])
    return return_list

def generate_list(days):
    return_list=[]
    for i in range(days):
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
    import_events("testinputs/events.csv")
    print "Igor V0.1"
    print "Today's tasks are:"
    for task in tasks_on_date(datetime.date.today()):
        print task

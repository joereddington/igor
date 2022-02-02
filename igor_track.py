import json
import re
import datetime
from time import time
from termcolor import cprint

class TaskDatabase():

    def __init__(self,filename):
        self.filename=filename
        self.structure={}
        self.load()

    def update(self, id_string):
        key=make_key(id_string)
        if key not in self.structure: 
            local={}
            local['firstseen']=time()
            self.structure[key]=local
        self.structure[key]['lastseen']=time()

    def age(self, id_string):
        key=make_key(id_string)
        if key in self.structure: 
            local=self.structure[key]
            age_in_seconds=time()-local['firstseen'] 
            age_in_days=age_in_seconds/(60*60*24)
            return age_in_days
        return -1 #TODO throw an error here

    def save(self):
        with open(self.filename, 'w') as filehandle:
            json.dump(self.structure, filehandle)
    
    def load(self):
        with open(self.filename, 'r') as filehandle:
            self.structure = json.load(filehandle)

    def update_current_tasks(self,todo_list): 
        self.todo_list=todo_list
        for task in todo_list: 
            self.update(task['task'])
        self.prune_stale_tasks()
        self.save()

    def prune_stale_tasks(self):
        seconds_in_day=24*60*60
        print("Size before was {}".format(len(list(self.structure.keys()))))
        for key in list(self.structure.keys()): #it's a list because otherwise you are deleting things from an itterator
            if time()-self.structure[key]['lastseen']>seconds_in_day:
                del self.structure[key] 
        print("Size after was {}".format(len(list(self.structure.keys()))))

    def get_current_tasks(self):
        for task in self.todo_list: 
            task['age']=self.age(task['task']) 
        return self.todo_list

def get_todo_list(todofilename):
    todo_list=[]
    with open(todofilename) as file:
        for line in file: 
            item={}
            item['task']=line.strip()
            todo_list.append(item) 
    return todo_list

def make_key(in_string):
    in_string=re.sub('^\(.\)','',in_string)
    in_string=re.sub(' [0-9][0-9] ','',in_string)
    return in_string.strip()

def print_tasks_by_age(todo_list): 
    red_tasks= [task for task in todo_list if task['age']>=7] 
    purple_tasks= [task for task in todo_list if task['age']>=3 and task['age']<7] 
    green_tasks= [task for task in todo_list if task['age']>1 and task['age']<=3]
    print("Purple Tasks")
    for task in purple_tasks: 
        cprint(task['task'],'blue')

    print("Red Tasks")
    for task in red_tasks: 
        cprint(task['task'],'red')

def write_age_of_tasks(todo_list,resultsname):
    red_tasks= [task for task in todo_list if task['age']>7] 
    purple_tasks= [task for task in todo_list if task['age']>3] 
    green_tasks= [task for task in todo_list if task['age']>1] 
    now = datetime.datetime.now()
    datestring=now.strftime("%Y-%m-%d")
    with open(resultsname, 'a') as f:
        f.write("{}, {}, {:.0f}, {}, {},  {}\n".format(len(todo_list),datestring,time(), len(green_tasks),len(purple_tasks),len(red_tasks)))


def run(todofilename,databasename,resultsname):
    database=TaskDatabase(databasename)
    database.update_current_tasks(get_todo_list(todofilename))
    write_age_of_tasks(database.get_current_tasks(),resultsname)
    print_tasks_by_age(database.get_current_tasks())

run("../todo.txt/todo.txt","database.json","results.txt")
run("../todo.txt/eqt.todo.txt","eqt.database.json","eqt.results.txt")

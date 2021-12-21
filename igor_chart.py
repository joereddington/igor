import json
import datetime
from time import time

class TaskDatabase():

    def __init__(self,filename):
        self.filename=filename
        self.structure={}
        self.load()

    def update(self, id_string):
        if id_string not in self.structure: 
            local={}
            local['firstseen']=time()
            local['lastseen']=time()
            self.structure[id_string]=local

    def age(self, id_string):
        if id_string in self.structure: 
            local=self.structure[id_string]
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
        for key in list(self.structure.keys()): #it's a list because otherwise you are deleting things from an itterator
            if time()-self.structure[key]['lastseen']:
                del self.structure[key] 

    def get_current_tasks(self):
        for task in self.todo_list: 
            task['age']=self.age(task['task']) 
        return self.todo_list

def get_todo_list():
    todo_list=[]
    with open("../todo.txt/todo.txt") as file:
        for line in file: 
            item={}
            item['task']=line.strip()
            todo_list.append(item) 
    return todo_list

def write_age_of_tasks(todo_list):
    red_tasks= [task for task in todo_list if task['age']>7] 
    purple_tasks= [task for task in todo_list if task['age']>3] 
    green_tasks= [task for task in todo_list if task['age']>1] 
    now = datetime.datetime.now()
    datestring=now.strftime("%Y-%m-%d")
    with open('results.txt', 'a') as f:
        f.write("{}, {}, {:.0f}, {}, {},  {}\n".format(len(todo_list),datestring,time(), len(green_tasks),len(purple_tasks),len(red_tasks)))

database=TaskDatabase("database.json")
database.update_current_tasks(get_todo_list())
write_age_of_tasks(database.get_current_tasks())

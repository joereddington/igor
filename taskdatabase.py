import json 
import re
import datetime
from time import time


def make_key(in_string):
    in_string=re.sub('^\(.\)','',in_string)
    in_string=re.sub(' [0-9][0-9] ','',in_string)
    return in_string.strip()

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

    def get_oldest(self):
        task_list=self.get_current_tasks()
        oldest=max(task_list, key=lambda x:x['age'])
        print("The task \"{}\" is {:.0f} days old".format(oldest['task'],oldest['age']))
        return oldest

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

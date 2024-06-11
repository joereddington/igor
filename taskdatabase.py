import json 
import re
import datetime
from time import time


def make_key(in_string):  # We remove the priority and time (which change quite often) when storing a task so the age is more accurate
    in_string=re.sub('^\(.\)','',in_string)
    in_string=re.sub(' [0-9][0-9] ','',in_string)
    return in_string.strip()

class TaskDatabase():

    def __init__(self,json_filename):
        self.filename=json_filename # We use the filename for loading and also saving so we need to keep it. 
        self.structure={}
        self.load() #Loads from the filename given  
        self.todo_list=[] # We initialise the current Todo list to the empty string TODO: why? 
        self.projects=""
        self.last_project_update=False

    def update_current_tasks(self,todo_list): # TODO - this should be part of the class initialisation - or a multiple 
        self.todo_list=todo_list
        for task in todo_list: 
            self.update_task(task['task'])
        self.prune_stale_tasks()
        self.save()


    def create_project_tasks(self, project_filename):
        new_tasks = ""
        with open(project_filename, 'r') as file:
            lines = file.readlines()
        for line in lines:
            line = line.strip()
            if not self.search_current_todo(line):
                new_task = f"(C) 04 Work out next task for project {line}"
               # self.todo_list.append({'task': new_task, 'age': 0})  This is for when we start properly adding
                new_tasks += new_task + "\n"
        return new_tasks.strip()


        return new_tasks


    def save(self):
        with open(self.filename, 'w') as filehandle:
            json.dump(self.structure, filehandle, indent=4)


    def save(self):
        wholedatabase = {
            'tasks': self.structure,
            'projects': self.projects,
            'lastupdate': self.last_project_update
        }
        with open(self.filename, 'w') as filehandle:
            json.dump(wholedatabase, filehandle, indent=4)

    def load(self):
        with open(self.filename, 'r') as filehandle:
            wholedatabase= json.load(filehandle)
            self.structure=wholedatabase['tasks']
            self.projects=wholedatabase['projects']
            self.last_project_update=wholedatabase['lastupdate']

    def search_current_todo(self, search_string): 
        if self.todo_list is False:
            print("Todo list NOT present")
            return 
        tasks=self.get_current_tasks() 
        for task in tasks: 
            if search_string in task['task']:
                return task['task']
        return False  #TODO this needs a test case 

    def update_task(self, id_string): # If this task isn't in the database add it, and if it is, update the 'lastseen' value
        key=make_key(id_string)
        if key not in self.structure: 
            local={}
            local['firstseen']=time()
            self.structure[key]=local
        self.structure[key]['lastseen']=time()

    def get_age_of_task(self, id_string): # TODO It would be nice if this was implicit 
        key=make_key(id_string)
        if key in self.structure: 
            local=self.structure[key]
            age_in_seconds=time()-local['firstseen'] 
            age_in_days=age_in_seconds/(60*60*24)
            return age_in_days
        print(f"Warning 'get_age_of_task' returned -1 for {id_string}")
        return -1 #TODO throw an error here (TODO find out how often this happens

    def print_oldest_in_current_tasks(self):
        task_list=self.get_current_tasks()
        oldest=max(task_list, key=lambda x:x['age'])
        print("The task \"{}\" is {:.0f} days old".format(oldest['task'],oldest['age']))
        return oldest


    def prune_stale_tasks(self):
        seconds_in_day=24*60*60
        #print("Size before pruning database of stale tasks was {}".format(len(list(self.structure.keys()))))
        for key in list(self.structure.keys()): #it's a list because otherwise you are deleting things from an itterator
            if time()-self.structure[key]['lastseen']>seconds_in_day:
                del self.structure[key] 
        #print("Size after was {}".format(len(list(self.structure.keys()))))

    def get_current_tasks(self):
        for task in self.todo_list: 
            task['age']=self.get_age_of_task(task['task']) 
        return self.todo_list

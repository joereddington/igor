import json
import os
import re
import datetime
from time import time
#from termcolor import cprint
from pathlib import Path
from taskdatabase import TaskDatabase

def get_todo_list(todofilename):
    todo_list=[]
    with open(todofilename) as file:
        for line in file: 
            print("there's a comment" )
            if "#" in line or len(line)<3:
                pass
            else:
                item={}
                item['task']=line.strip()
                todo_list.append(item) 
    return todo_list


def print_tasks_by_age(todo_list): 
    from termcolor import cprint
    red_tasks= [task for task in todo_list if task['age']>=7] 
    purple_tasks= [task for task in todo_list if task['age']>=3 and task['age']<7] 
    green_tasks= [task for task in todo_list if task['age']>1 and task['age']<=3]
    print("Green Tasks")
    for task in green_tasks: 
        cprint(task['task'],'green')

    print("Purple Tasks")
    for task in purple_tasks: 
        cprint(task['task'],'magenta')

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


def display(todofilename,databasename,resultsname):
    database=TaskDatabase(databasename)
    database.update_current_tasks(get_todo_list(todofilename))
    write_age_of_tasks(database.get_current_tasks(),resultsname)
    print_tasks_by_age(database.get_current_tasks())
    database.get_oldest()



from pathlib import Path
script_path = os.path.dirname(os.path.abspath(__file__))+"/"
display(script_path+"../todo.txt/todo.txt",script_path+"database.json",script_path+"results.txt")
display(script_path+"../todo.txt/eqt.todo.txt",script_path+"eqt.database.json",script_path+"eqt.results.txt")

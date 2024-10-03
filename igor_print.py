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


def display(database,resultsname):
    write_age_of_tasks(database.get_current_tasks(),resultsname)
    print_tasks_by_age(database.get_current_tasks())
    database.print_oldest_in_current_tasks()

def combined_write():
    all_tasks=[]
    all_tasks.extend(database.get_current_tasks())
    all_tasks.extend(rhul_database.get_current_tasks())
    all_tasks.extend(eqt_database.get_current_tasks())
    write_age_of_tasks(all_tasks,script_path+"outputs/all.results.txt")


from pathlib import Path

if __name__ == "__main__":
    script_path = os.path.dirname(os.path.abspath(__file__))+"/"

    database=TaskDatabase(script_path+"databases/database.json") #Main database
    print("Todo database loaded")
    database.update_current_tasks(get_todo_list(script_path+"../todo.txt/todo.txt"))
    rhul_database=TaskDatabase(script_path+"databases/rhul.database.json")
    print("rhul database loaded")
    rhul_database.update_current_tasks(get_todo_list(script_path+"../diary/rhul.todo.txt"))
    eqt_database=TaskDatabase(script_path+"databases/eqt.database.json")
    print("eqt database loaded")
    eqt_database.update_current_tasks(get_todo_list(script_path+"../todo.txt/eqt.todo.txt"))

    display(database,script_path+"outputs/results.txt")
    print("----------------------------------")
    display(rhul_database,script_path+"outputs/rhul.results.txt")
    print("----------------------------------")
    display(eqt_database,script_path+"outputs/eqt.results.txt")
    print("----------------------------------")
    combined_write()

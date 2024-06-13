import json
import os
import re
import datetime
from time import time
#from termcolor import cprint
from pathlib import Path
from taskdatabase import TaskDatabase
from pathlib import Path
from igor_print import get_todo_list

script_path = os.path.dirname(os.path.abspath(__file__))+"/"

database=TaskDatabase(script_path+"databases/database.json") #Main database
database.update_current_tasks(get_todo_list(script_path+"../todo.txt/todo.txt"))
rhul_database=TaskDatabase(script_path+"databases/rhul.database.json")
rhul_database.update_current_tasks(get_todo_list(script_path+"../diary/rhul.todo.txt"))
eqt_database=TaskDatabase(script_path+"databases/eqt.database.json")
eqt_database.update_current_tasks(get_todo_list(script_path+"../todo.txt/eqt.todo.txt"))

print(eqt_database.create_project_tasks("art_project_list.txt"))

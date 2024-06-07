import unittest
import json
import os
from unittest.mock import patch, mock_open, MagicMock
from time import time
from taskdatabase import TaskDatabase, make_key  # Assuming the above code is in a file named task_database.py

class TestTaskDatabase(unittest.TestCase):

    def setUp(self):
        # Mock JSON content
        self.mock_json_content = {
            "task1": {
                "firstseen": time() - 100000,  # Arbitrary past time
                "lastseen": time() - 50000
            },
            "task2": {
                "firstseen": time() - 200000,
                "lastseen": time() - 100000
            }
        }
        self.mock_json_filename = 'mock_tasks.json'
        self.mock_todo_list = [
            {'task': '(A) Buy groceries 01', 'age': 1},
            {'task': '(B) Clean the house 02', 'age': 2},
        ]
        self.mock_json_content_str = json.dumps(self.mock_json_content)

        # Mock opening files
        self.open_patcher = patch('builtins.open', mock_open(read_data=self.mock_json_content_str))
        self.open_patcher.start()

        # Mock time
        self.time_patcher = patch('time.time', MagicMock(side_effect=[time(), time() + 1000]))
        self.mock_time = self.time_patcher.start()

        self.db = TaskDatabase(self.mock_json_filename)
    
    def tearDown(self):
        self.open_patcher.stop()
        self.time_patcher.stop()
        if os.path.exists(self.mock_json_filename):
            os.remove(self.mock_json_filename)

    def test_make_key(self):
        result = make_key('(A) Task 01 ')
        self.assertEqual(result, 'Task')

    def test_load(self):
        self.db.load()
        self.assertEqual(self.db.structure, self.mock_json_content)

    def test_save(self):
        self.db.save()
        with open(self.mock_json_filename, 'r') as filehandle:
            data = json.load(filehandle)
        self.assertEqual(data, self.mock_json_content)

    def test_update_current_tasks(self):
        self.db.update_current_tasks(self.mock_todo_list)
        self.assertEqual(len(self.db.structure), 3)  # I think there were two tasks, then two were added, and one was pruned. 

    def test_search_current_todo_found(self):
        self.db.update_current_tasks(self.mock_todo_list)
        result = self.db.search_current_todo('Buy groceries')
        self.assertEqual(result, '(A) Buy groceries 01')

    def test_search_current_todo_not_found(self):
        self.db.update_current_tasks(self.mock_todo_list)
        result = self.db.search_current_todo('Not existing task')
        self.assertFalse(result)

    def test_update_task(self):
        self.db.update_task('(A) 03 New Task' )
        self.assertIn('New Task', self.db.structure)

    def test_get_age_of_task(self):
        self.db.update_task('(A) New Task 03')
        age = self.db.get_age_of_task('(A) New Task 03')
        self.assertIsInstance(age, float)

    def test_print_oldest_in_current_tasks(self):
        self.db.update_current_tasks(self.mock_todo_list)
        oldest = self.db.print_oldest_in_current_tasks()
        self.assertEqual(oldest['task'], '(B) Clean the house 02')

    def test_prune_stale_tasks(self):
        self.db.prune_stale_tasks()
        self.assertEqual(len(self.db.structure), 1)  # Since one task should be pruned

    def test_get_current_tasks(self):
        self.db.update_current_tasks(self.mock_todo_list)
        tasks = self.db.get_current_tasks()
        self.assertEqual(len(tasks), 2)
        for task in tasks:
            self.assertIn('age', task)

if __name__ == '__main__':
    unittest.main()


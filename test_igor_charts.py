from unittest import TestCase
import unittest
import datetime
import igor
import igor_chart

class igor_chart_test(TestCase):

    def test_read_file(self):
       "only checking if it reads the right size"
       igor.events=[]
       igor.import_events("testinputs/todo.txt")
       self.assertEqual(len(igor.events),4)


    def test_write_a_file(self):
        "Just put some information into a file"
        igor.events=[]
        igor.import_events("testinputs/todo.txt")
        igor_chart.save(igor.events,"testoutputs/one.json")  
        
    def test_load(self):
        "Just put some information into a file"
        events=igor_chart.load("testoutputs/one.json")  
        self.assertEqual(len(events),4)
        
# what do I need to write tests for? 
# return the ordinal for a date
# return the events for an ordinal 
# print the events for an ordinal 


if __name__=="__main__":
    unittest.main()

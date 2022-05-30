from unittest import TestCase
import unittest
import datetime
import igor
import igor_chart

class igor_chart_test(TestCase):

    def test_key(self):
        result=igor_chart.make_key("(A) Hopeful")        
        self.assertEqual(result,"Hopeful")

    def test_key2(self):
        result=igor_chart.make_key("(A) 05 Hopeful")        
        self.assertEqual(result,"Hopeful")


        
# what do I need to write tests for? 
# return the ordinal for a date
# return the events for an ordinal 
# print the events for an ordinal 


if __name__=="__main__":
    unittest.main()

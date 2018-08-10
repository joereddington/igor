from unittest import TestCase
import unittest
import igor

class igor_test(TestCase):

    def test_read_file(self):
       "only checking if it reads the right size"
       igor.import_events("testinputs/events.csv")
       self.assertEqual(len(igor.events),2)

if __name__=="__main__":
    unittest.main()

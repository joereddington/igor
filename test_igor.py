from unittest import TestCase
import unittest
import datetime
import igor

class igor_test(TestCase):

    def test_read_file(self):
       "only checking if it reads the right size"
       igor.events=[]
       igor.import_events("testinputs/events.csv")
       self.assertEqual(len(igor.events),2)

    def test_read_file_and_get_priority(self):
       "only checking if it reads the right size"
       igor.events=[]
       igor.import_events("testinputs/events.csv")
       self.assertEqual(int(igor.events[0][0]),1)


    def test_events_in_ten_days(self):
       igor.events=[]
       igor.import_events("testinputs/events.csv")
       events=igor.generate_list(10)
       self.assertEqual(len(events),12)



    def test_events_on_this_say(self):
        current_date = datetime.date.today()
        target_date=datetime.date.fromordinal(100)
        igor.events=[]
        igor.import_events("testinputs/events.csv")
        tasks=igor.tasks_on_date(target_date)
        self.assertEqual(len(tasks),2)




if __name__=="__main__":
    unittest.main()

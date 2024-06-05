from unittest import TestCase
import unittest
import datetime
import art

class art_test(TestCase):

    def test_read_file(self):
       "only checking if it reads the right size"
       art.events=[]
       art.import_events("testinputs/events.csv")
       self.assertEqual(len(art.events),2)

    def test_read_file_and_get_priority(self):
       "only checking if it reads the right size"
       art.events=[]
       art.import_events("testinputs/events.csv")
       self.assertEqual(int(art.events[0][0]),1)


    def test_events_in_ten_days(self):
       art.events=[]
       art.import_events("testinputs/events.csv")
       events=art.generate_list(10)
       self.assertEqual(len(events),12)



    def test_events_on_this_day_1(self):
        current_date = datetime.date.today()
        target_date=datetime.date.fromordinal(105)
        art.events=[]
        art.import_events("testinputs/events.csv")
        tasks=art.tasks_on_date(target_date)
        self.assertEqual(len(tasks),2)

    def test_events_on_this_day_2(self):
        current_date = datetime.date.today()
        target_date=datetime.date.fromordinal(100)
        art.events=[]
        art.import_events("testinputs/events.csv")
        tasks=art.tasks_on_date(target_date)
        self.assertEqual(len(tasks),1)
    
    def test_get_events_for_this_ordinal(self):
        ordinal=7
        tasks=art.tasks_on_date(ordinal)
        self.assertEqual(len(tasks),2)

    def test_tasks_since(self):
        start=7
        end=15
        tasks=art.tasks_since(start,end)
        self.assertEqual(len(tasks),10)

    def test_extract_number(self):
        #TODO - write the code that goes with this   
        input_string = ") is 42 and the second number is 1234"
        expected_output = 42
        assert extract_number(input_string) == expected_output

        input_string = "The number is 1"
        expected_output = 1
        assert extract_number(input_string) == expected_output

        input_string = "No number found"
        expected_output = None
        assert extract_number(input_string) == expected_output

#I'll be reading in a list of projects and checking to see if they are in the list of tasks. It's NOT actually hard right?  


if __name__=="__main__":
    unittest.main()

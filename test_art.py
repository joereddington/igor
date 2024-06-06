from unittest import TestCase
import unittest
import datetime
import art
import how_long_to_complete_a_todo_list

class art_test(TestCase):

    def test_read_file(self):
       "only checking if it reads the right size"
       events=art.import_events("testinputs/events.csv")
       self.assertEqual(len(events),2)

    def test_read_file_and_get_priority(self):
       "only checking if it reads the right size"
       events=art.import_events("testinputs/events.csv")
       self.assertEqual(int(events[0][0]),1)


    def test_events_on_this_day_1(self):
        current_date = datetime.date.today()
        target_date=datetime.date.fromordinal(105)
        events=art.import_events("testinputs/events.csv")
        tasks=art.tasks_on_date(events,target_date)
        self.assertEqual(len(tasks),2)

    def test_events_on_this_day_2(self):
        current_date = datetime.date.today()
        target_date=datetime.date.fromordinal(100)
        events=art.import_events("testinputs/events.csv")
        tasks=art.tasks_on_date(events,target_date)
        self.assertEqual(len(tasks),1)
    
    def test_get_events_for_this_ordinal(self):
        ordinal=7
        events=art.import_events("testinputs/events.csv")
        tasks=art.tasks_on_date(events,ordinal)
        self.assertEqual(len(tasks),2)

    def test_tasks_since(self):
        start=7
        end=15
        events=art.import_events("testinputs/events.csv")
        tasks=art.tasks_since(events,start,end)
        self.assertEqual(len(tasks),10)

    def test_extract_number(self):
        #TODO - write the code that goes with this   
        input_string = ") is 42 and the second number is 1234"
        expected_output = 42
        assert how_long_to_complete_a_todo_list.find_two_digit_number(input_string) == expected_output

        input_string = "No number found"
        expected_output = None
        assert how_long_to_complete_a_todo_list.find_two_digit_number(input_string) == expected_output

#I'll be reading in a list of projects and checking to see if they are in the list of tasks. It's NOT actually hard right?  


if __name__=="__main__":
    unittest.main()

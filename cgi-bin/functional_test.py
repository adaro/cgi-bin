#No shebang line. Run via cmd line:
#$ python functional_test.py
###
#Functional Unit Test
#tests instance methods of
#server.NprFeed class
###

#import unittest std lib
import unittest
#import NprFeed class from server module
from server import NprFeed

class MyTest(unittest.TestCase):
    """
    unit test class used to test return values
    and data structures from instance methods
    """
    def is_instance_assertion(self, data, data_type, msg_str):
        #uses assertIsInstance inherited from base class to determine
        #if the data argument is an instance of the data_type 
        self.assertIsInstance(data, data_type, msg=msg_str)
        
    def bool_assertion(self, data, msg_str):
        #uses assertTrue inherited from base
        #class to determine if data expression returns True.
        self.assertTrue(data, msg=msg_str)
                
    def test_entry_list_type(self):
        #instantiate class, run instance method and
        #is_instance_assertion to determine if entry_list
        #is of type: list 
        wd_instance = NprFeed()        
        entry_list = wd_instance.return_list()
        msg_str = "entries is not of type: list"
        self.is_instance_assertion(entry_list, list, msg_str)

    def test_items_type(self):
        #instantiate class, run instance method and
        #is_instance_assertion to determine if items
        #is of type: list        
        wd_instance = NprFeed() 
        items = wd_instance.fetch_item()
        msg_str = "items is not of type: list"
        self.is_instance_assertion(items, list, msg_str)

    def test_loop_items(self):
        #instantiate class, run instance method and
        #bool_assertion to determine if bool_expr
        #returns True         
        wd_instance = NprFeed()
        items = wd_instance.fetch_item()
        items_list = wd_instance.loop_items(items)
        items_length = len(items_list)
        bool_expr = items_length > 0
        msg_str = "length of items_list is equal to: 0"
        self.bool_assertion(bool_expr, msg_str)
        
        
#Run main. This will run all methods inside of
#MyTest class that start with "test"
if __name__ == '__main__':
    unittest.main()

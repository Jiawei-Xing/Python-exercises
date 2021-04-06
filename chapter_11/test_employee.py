import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    
    def setUp(self):
        self.my_employee = Employee('Jiawei', 22, 30000)
        self.increment = 6000
    
    def test_give_default_raise(self):
        self.my_employee.give_raise()
        self.assertEqual(35000, self.my_employee.salary)
    
    def test_give_custom_raise(self):
        self.my_employee.give_raise(6000)
        self.assertEqual(36000, self.my_employee.salary)
        
unittest.main()

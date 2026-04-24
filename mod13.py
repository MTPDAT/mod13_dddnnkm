import unittest
import re
from datetime import datetime

# Simple validation functions
def validate_symbol(symbol):
    if not symbol or not symbol.isalpha() or not symbol.isupper() or not (1 <= len(symbol) <= 7):
        return False
    return True

def validate_chart_type(chart_type):
    if not chart_type or len(chart_type) != 1 or not chart_type.isdigit() or chart_type not in ['1', '2']:
        return False
    return True

def validate_time_series(time_series):
    if not time_series or len(time_series) != 1 or not time_series.isdigit() or time_series not in ['1', '2', '3', '4']:
        return False
    return True

def validate_date(date_string):
    if not date_string or not re.match(r'^\d{4}-\d{2}-\d{2}$', date_string):
        return False
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Unit tests
class TestInputs(unittest.TestCase):
    
    def test_symbol_valid(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("GOOGL"))
        self.assertTrue(validate_symbol("A"))
        self.assertTrue(validate_symbol("ABCDEFG"))
    
    def test_symbol_invalid(self):
        self.assertFalse(validate_symbol(""))      
        self.assertFalse(validate_symbol("aapl"))  
        self.assertFalse(validate_symbol("AAPL1")) 
        self.assertFalse(validate_symbol("ABCDEFGH"))
        self.assertFalse(validate_symbol("AAP$"))
    
    # Chart type tests
    def test_chart_type_valid(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))
    
    def test_chart_type_invalid(self):
        self.assertFalse(validate_chart_type(""))   
        self.assertFalse(validate_chart_type("3"))  
        self.assertFalse(validate_chart_type("12"))
        self.assertFalse(validate_chart_type("a")) 
    
    # Time series tests
    def test_time_series_valid(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))
    
    def test_time_series_invalid(self):
        self.assertFalse(validate_time_series(""))  
        self.assertFalse(validate_time_series("5")) 
        self.assertFalse(validate_time_series("12")) 
        self.assertFalse(validate_time_series("a"))  
    
    # Start date tests
    def test_start_date_valid(self):
        self.assertTrue(validate_date("2023-01-01"))
        self.assertTrue(validate_date("2024-12-31"))
        self.assertTrue(validate_date("2024-02-29")) 
    
    def test_start_date_invalid(self):
        self.assertFalse(validate_date(""))           
        self.assertFalse(validate_date("2023/01/01"))
        self.assertFalse(validate_date("01-01-2023")) 
        self.assertFalse(validate_date("2023-13-01")) 
        self.assertFalse(validate_date("2023-01-32")) 
    
    # End date tests
    def test_end_date_valid(self):
        self.assertTrue(validate_date("2023-12-31"))
        self.assertTrue(validate_date("2024-01-15"))
    
    def test_end_date_invalid(self):
        self.assertFalse(validate_date(""))           
        self.assertFalse(validate_date("2023-02-30"))
        self.assertFalse(validate_date("23-12-31"))   

if __name__ == '__main__':
    unittest.main()
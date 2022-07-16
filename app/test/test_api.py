import pytest
from app.request_api import Request
# from sys import path
# from os.path import realpath
# path.append(realpath("./"))
#from  request_api import Request
                
class TestRequest:
    def test_get_response(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout=3)
        assert instance.get_response() == 200, "Peticion expected to be 200"

    def test_get_response_error_timeout_negative(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout=-3)
        assert instance.get_response() == 'Error', "Peticion not expected timeout can not be negative"
    
    def test_get_response_error_timeout_string(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout="a")
        assert instance.get_response() == 'Error', "Peticion not expected timeout can not be string"
    
    def test_get_response_error_timeout_none(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout=None)
        assert instance.get_response() == 200, "Peticion expected timeout can be None"

    def test_get_response_error_date(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-1"}, timeout=3)
        assert instance.get_response() == 422, "Peticion not expected date can not be 1 digit must be 2 digits Ex: 2020-12-01"

    def test_get_response_error_timeout_float(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-01"}, timeout=1.1)
        assert instance.get_response() == 200, "Peticion expected timeout can be float"

    def test_get_response_error_day_out_of_range(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-12-32"}, timeout=3)
        assert instance.get_response() == 422, "Peticion not expected date can not be out of range"
    
    def test_get_response_error_month_out_of_range(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2020-13-01"}, timeout=3)
        assert instance.get_response() == 422, "Peticion not expected date can not be out of range"
    
    def test_get_response_error_year_out_of_range(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"2040-12-01"}, timeout=3)
        assert instance.get_response() == 200, "Valid date but it is greater than the actual year"

    def test_get_response_error_year_out_of_range_2(self):
        instance = Request(url='http://api.tvmaze.com/schedule/web', params={"date":"1900-12-01"}, timeout=3)
        assert instance.get_response() == 200, "valid date but is too old for have information"
    
    
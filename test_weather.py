#tes_weather.py

import pytest
import weather 

#locurl="http://api.ipstack.com/check?access_key=01ba0bb834c723d9d47f061780376e45"

    

def test_temp1():
    ts = 0
    val = weather.temp_conv(ts)
    exp = -459
    assert int(val) == exp

def test_temp2():
    ts = -2000
    val = weather.temp_conv(ts)
    exp = -4059
    assert int(val) == exp

def test_temp3():
    ts = 30000
    val = weather.temp_conv(ts)
    exp = 53540
    assert int(val) == exp

def test_temp4():
    ts = 0.0
    val = weather.temp_conv(ts)
    exp = -459
    assert int(val) == exp

def test_temp5():
    ts = -2000.3
    val = weather.temp_conv(ts)
    exp = -4059
    assert int(val) == exp



#def teardown_method(self, method):
 #       # This method is being called after each test case, and it will revert input back to original function
  #      weather.input = input  
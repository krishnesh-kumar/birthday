import birthday as b
import pytest

#This test case may fails because your current date may be changed.
#According to that you have to change your output string 

test_str=list()
with open("F:/Try_python/LTTS_PYTHON/python2/project/test_data.txt") as data:
    for date in data:
        test_str.append((date.split(",")[0],date.split(",")[1].strip()))


@pytest.mark.parametrize('date,string',test_str)
def test_reminder(date,string):
    c_date=b.Bdate(date)    
    assert c_date.reminder().lower()==string.lower()

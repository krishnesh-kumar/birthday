import birthday as b
import pytest

#This is not working fine only last test case got executed.

##def test_str(fh):
##    for date in fh:
##        yield [(date.split(",")[0],date.split(",")[1].strip())]
##
##with open("F:/Try_python/LTTS_PYTHON/python2/project/Diff_current_date/test_file.txt") as data:
##    for i in test_str(data):
##        @pytest.mark.parametrize('date,string',i)
##        def test_reminder(date,string):
##            c_date=b.todaydate(date)
##            assert c_date.reminder().lower()==string.lower()


test_str=list()
with open("F:/Try_python/LTTS_PYTHON/python2/project/Diff_current_date/test_file.txt") as data:
    for date in data:
        test_str.append((date.split(",")[0],date.split(",")[1].strip()))

@pytest.mark.parametrize('date,string',test_str)
def test_reminder(date,string):
    c_date=b.todaydate(date)
    assert c_date.reminder().lower()==string.lower()


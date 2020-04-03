import birthday as b
import pytest
test_str=[("15-03-1995","2 Weeks ago"),
    ]
@pytest.mark.parametrize('date,string',test_str)
def test_reminder(date,string):
    #for date , string in test_str:
        #c_date=b.Bdate(date)
        #assert c_date.reminder().lower()==string.lower()
    c_date=b.Bdate(date)    
    assert c_date.reminder().lower()==string.lower()

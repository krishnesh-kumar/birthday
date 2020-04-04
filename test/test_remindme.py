import birthday as b
import pytest
test_str=[("01-01-2020","2 month from now"),
          ("31-01-2020","2 month from now"),
          ("01-02-2020","Next month"),
          ("13-02-2020","Next month"),
          ("14-02-2020","30 days from now"),
          ("15-02-2020","Next month"),
          ("16-02-2020","28 days from now"),
          ("17-02-2020","After 3 weeks"),
          ("22-02-2020","After 3 weeks"),
          ("23-02-2020","3 weeks from now"),
          ("24-02-2020","20 days from now"),
          ("29-02-2020","15 days from now"),
          ("01-03-2020","2 weeks from now"),
          ("02-03-2020","Next Sunday"),
          ("08-03-2020","Next Sunday"),
          ("09-03-2020","Coming sunday"),
          ("12-03-2020","Coming Sunday"),
          ("13-03-2020","Day After Tommorow"),
          ("14-03-2020","Tomorrow"),
          ("15-03-2020","Today"),
          ("16-03-2020","Yesterday"),
          ("17-03-2020","Day before yesterday"),
          ("18-03-2020","3 Days back"),
          ("21-03-2020","6 days back"),
          ("22-03-2020","Last Sunday"),
          ("23-03-2020","In Last week"),
          ("28-03-2020","In last week"),
          ("29-03-2020","2 weeks ago"),
          ("04-04-2020","2 weeks ago"),
          ("05-04-2020","3 weeks ago"),
          ("11-04-2020","3 weeks ago"),
          ("12-04-2020","Almost a month ago"),
          ("14-04-2020","Almost a month ago"),
          ("15-04-2020","Last Month"),
          ("30-04-2020","Last month"),
          ("01-05-2020","2 month ago"),
          ("31-05-2020","2 month ago"),
          ("1-08-2020","5 month ago"),
          ("01-12-2020","9 month ago"),
    ]
@pytest.mark.parametrize('date,string',test_str)
def test_reminder(date,string):
    #for date , string in test_str:
        #c_date=b.Bdate(date)
        #assert c_date.reminder().lower()==string.lower()
    c_date=b.todaydate(date)
    print(c_date.reminder())
    print(string)
    assert c_date.reminder().lower()==string.lower()

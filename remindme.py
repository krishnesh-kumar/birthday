import sys
import birthday as b

if len(sys.argv)==2:
    date=sys.argv[1]
b_date=b.Bdate(date)
b_date.reminder()

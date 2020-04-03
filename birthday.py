import datetime as d
import math

'''
This file is used to remind user about the b'day he entered
'''

class Bdate:
    
    '''
    Enter the date in dd-mm-yy formate
    '''

    def __init__(self,date):
        #date="15-03-1995"
        bday_l =  date.split("-")
        self.tdate =  d.date.today()
        #date1_l=date1.split("-")
        #self.tdate=d.date(int(date1_l[2]),int(date1_l[1]),int(date1_l[0]))
        bday_l[2] =  self.tdate.strftime("%Y")
        self.bday_c =  d.date(int(bday_l[2]),int(bday_l[1]),int(bday_l[0]))
        self.days =  self.bday_c-self.tdate
        if str(self.days)=='0:00:00':
            self.days=0
        self.days =  int(str(self.days).split()[0])
        self.ago_month =  int(self.tdate.strftime("%m"))-int(self.bday_c.strftime("%m"))
        #self.from_now_month =  abs(self.ago_month)
        self.bdate=date

    def reminder(self):
        '''
        This function contain the main logic of reminder app.
        '''
    #************************B'DAY IS OVER********************************************
        
        if self.days==-1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("yesterday")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "yesterday"

        elif self.days==-2:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("day before yesterday")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "day before yesterday"
                
        elif -6<=self.days<=-3:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"{abs(self.days)} days back")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{abs(self.days)} days back"

        elif self.days==-7:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"last {self.bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"last {self.bday_c.strftime('%A')}"

        elif -13<=self.days<=-8:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("Last week")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "In Last week"

        elif -20<=self.days<=-14:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("2 weeks ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "2 weeks ago"
            
        elif -27<=self.days<=-21:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("3 weeks ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "3 weeks ago"    
            
        elif -31<self.days<=-28:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("Almost a month ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "Almost a month ago"

        elif self.days<=-31 and self.ago_month==1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("last month")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "last month"
            
        elif self.days<-31:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"{self.ago_month} month ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{self.ago_month} month ago"
            
        #************************TODAY IS B'DAY**********************************************
        elif self.days==0:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("TODAY")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "TODAY"
            
        #************************B'DAY STILL TO COME*****************************************

        elif self.days==1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("Tomorrow")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "Tomorrow"
            
        elif self.days==2:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("day after tommorow")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "day after tommorow"

        elif 3<=self.days<=6:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"coming {self.bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"coming {self.bday_c.strftime('%A')}"
        
        elif 7<=self.days<=13:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"Next {self.bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"Next {self.bday_c.strftime('%A')}"
        
        elif 15<=self.days<=20 or self.days==30 or self.days==28:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"{self.days} days from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{self.days} days from now"
        
        elif self.days==14:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("2 weeks from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "2 weeks from now"
        
        elif self.days==21:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("3 Weeks from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "3 Weeks from now"
        
        elif 22<=self.days<=27:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("After 3 weeks")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "After 3 weeks"
        
        elif (31<=self.days<=43 or self.days==29):
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("Next month")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "Next month"

        elif 44<=self.days<=74:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"{math.ceil(self.days/30)} month from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{2} month from now"

        elif self.days>74 and self.days/30>1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print(f"{math.ceil(self.days/30)} month from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{math.ceil(self.days/30)} month from now"
        

if __name__=="__main__":    
    b=Bdate("1-1-1995")
    print(b.reminder())

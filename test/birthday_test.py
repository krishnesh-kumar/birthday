import datetime as d
import math

'''
This file is used to remind user about the b'day he entered
'''

class todaydate:
    
    '''
    Enter the date in dd-mm-yy formate
    '''

    def __init__(self,date1):
        date="15-03-1995"
        bday_l =  date.split("-")
        #self.tdate =  d.date.today()
        date1_l=date1.split("-")
        self.tdate=d.date(int(date1_l[2]),int(date1_l[1]),int(date1_l[0]))
        bday_l[2] =  self.tdate.strftime("%Y")
        self.bday_c =  d.date(int(bday_l[2]),int(bday_l[1]),int(bday_l[0]))
        self.days =  self.bday_c-self.tdate
        if str(self.days)=='0:00:00':
            self.days=0
        self.days =  int(str(self.days).split()[0])
        self.ago_month =  int(self.tdate.strftime("%m"))-int(self.bday_c.strftime("%m"))
        #self.from_now_month =  abs(self.ago_month)
        self.bdate=date
        self.bday_dict={
                        
                        -1:"yesterday",
                        
                        -2:"day before yesterday",
                        
                        -3:f"{abs(self.days)} days back",-4:f"{abs(self.days)} days back",
                        -5:f"{abs(self.days)} days back",-6:f"{abs(self.days)} days back",
                        
                        -7:f"last {self.bday_c.strftime('%A')}",
                        
                        -8:"In Last week",-9:"In Last week",-10:"In Last week",-11:"In Last week",
                        -12:"In Last week",-13:"In Last week",
                        
                        -14:"2 weeks ago",-15:"2 weeks ago",-16:"2 weeks ago",-17:"2 weeks ago",
                        -18:"2 weeks ago",-19:"2 weeks ago",-20:"2 weeks ago",
                        
                        -21:"3 weeks ago",-22:"3 weeks ago",-23:"3 weeks ago",-24:"3 weeks ago",
                        -25:"3 weeks ago",-26:"3 weeks ago",-27:"3 weeks ago",
                        
                        -28:"Almost a month ago",-29:"Almost a month ago",-30:"Almost a month ago",
                        
                        -31:"last month",
                        
                        0:"Today",
                        
                        1:"Tomorrow",
                        
                        2:"day after tommorow",
                        
                        3:f"coming {self.bday_c.strftime('%A')}",4:f"coming {self.bday_c.strftime('%A')}",
                        5:f"coming {self.bday_c.strftime('%A')}",6:f"coming {self.bday_c.strftime('%A')}",
                        
                        7:f"Next {self.bday_c.strftime('%A')}",8:f"Next {self.bday_c.strftime('%A')}",
                        9:f"Next {self.bday_c.strftime('%A')}",10:f"Next {self.bday_c.strftime('%A')}",
                        11:f"Next {self.bday_c.strftime('%A')}",12:f"Next {self.bday_c.strftime('%A')}",
                        13:f"Next {self.bday_c.strftime('%A')}",
                        
                        14:"2 weeks from now",
                        
                        15:f"{self.days} days from now",16:f"{self.days} days from now",
                        17:f"{self.days} days from now",18:f"{self.days} days from now",
                        19:f"{self.days} days from now",20:f"{self.days} days from now",
                        28:f"{self.days} days from now",
                        30:f"{self.days} days from now",
                        
                        21:"3 Weeks from now",22:"After 3 weeks",23:"After 3 weeks",
                        24:"After 3 weeks",25:"After 3 weeks",26:"After 3 weeks",27:"After 3 weeks",
                        
                        29:"Next month",31:"Next month",32:"Next month",33:"Next month",
                        34:"Next month",35:"Next month",36:"Next month",37:"Next month",
                        38:"Next month",39:"Next month",40:"Next month",41:"Next month",
                        42:"Next month",43:"Next month",

                        44:f"{2} month from now",45:f"{2} month from now",46:f"{2} month from now",
                        47:f"{2} month from now",48:f"{2} month from now",49:f"{2} month from now",
                        50:f"{2} month from now",51:f"{2} month from now",52:f"{2} month from now",
                        53:f"{2} month from now",54:f"{2} month from now",55:f"{2} month from now",
                        56:f"{2} month from now",57:f"{2} month from now",58:f"{2} month from now",
                        59:f"{2} month from now",60:f"{2} month from now",61:f"{2} month from now",
                        62:f"{2} month from now",63:f"{2} month from now",64:f"{2} month from now",
                        65:f"{2} month from now",66:f"{2} month from now",67:f"{2} month from now",
                        68:f"{2} month from now",69:f"{2} month from now",70:f"{2} month from now",
                        71:f"{2} month from now",72:f"{2} month from now",73:f"{2} month from now",
                        74:f"{2} month from now",
                        
                        }
    def reminder(self):
        '''
        This function contain the main logic of reminder app.
        '''
    
    #************************B'DAY IS OVER********************************************
        
        if -30<=self.days<=-1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return self.bday_dict[self.days]
        
        elif self.days<=-31 and self.ago_month==1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            #print("last month")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return "last month"
            
        elif self.days<-31:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{self.ago_month} month ago"
            
    #************************B'DAY STILL TO COME*****************************************
        
        elif 0<=self.days<=74:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return self.bday_dict[self.days]
            
        elif self.days>=75 and self.days/30>1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
            return f"{math.ceil(self.days/30)} month from now"
        

if __name__=="__main__":    
    b=todaydate("1-1-1995")
    print(b.reminder())

import datetime as d

'''
This file is used to remind user about the b'day he entered
'''

class Bdate:
    '''
    Enter the date in dd-mm-yy formate
    '''
    def __init__(self,date):
        
        bday_l =  date.split("-")
        self.tdate =  d.date.today()
        bday_l[2] =  self.tdate.strftime("%Y")
        self.bday_c =  d.date(int(bday_l[2]),int(bday_l[1]),int(bday_l[0]))
        self.days =  self.bday_c-self.tdate
        self.days =  int(str(self.days).split()[0])
        self.ago_month =  int(self.tdate.strftime("%m"))-int(self.bday_c.strftime("%m"))
        self.from_now_month =  abs(self.ago_month)
        self.bdate=date

    def reminder(self):
    #************************B'DAY IS OVER********************************************
        '''
        This function will remind the user about the b'day.
        '''
        if self.days==-1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("yesterday")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days==-2:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("day before yesterday")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif -6<=self.days<=-3:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"{abs(self.days)} days back")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days==-7:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"last {self.bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif -13<=self.days<=-8:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("Last week")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif -20<=self.days<=-14:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("2 weeks ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif -27<=self.days<=-21:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("3 weeks ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif -31<=self.days<=-28:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("Almost a month ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days<-31 and self.ago_month==1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("last month")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days<-31:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"{ago_month} month ago")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        #************************B'DAY STILL TO COME*****************************************

        elif self.days==1:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("Tomorrow")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days==2:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("day after tommorow")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif 3<=self.days<=6:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"coming {self.bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif 7<=self.days<=13:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"Next {bday_c.strftime('%A')}")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif 15<=self.days<=20 or self.days==30 or self.days==28:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"{self.days} days from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days==14:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("2 weeks from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days==21:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("3 Weeks from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif 17<=self.days<=22:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("After 3 weeks")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")
        
        #NOT PERFECT CONDITIONS NEED TO BE MODIFIDED
        
        #(int(bday_c.strftime("%d"))==int(tdate.strftime("%d")) and 
        elif (31<=self.days<=43):
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print("Next month")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")

        elif self.days>43 and self.from_now_month>=2:
            print(f"{self.tdate.strftime('%d')}-{self.tdate.strftime('%b')}-{self.tdate.strftime('%Y')}")
            print(f"{self.from_now_month} month from now")
            print(f"on {self.bday_c.strftime('%A')} {self.bday_c.strftime('%d')}th of {self.bday_c.strftime('%B')}")


if __name__=="__main__":    
    b=Bdayreminder("3-5-1995")
    b.reminder()

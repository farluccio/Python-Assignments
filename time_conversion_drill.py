##Created by Eric Farley Python 2.7.13
##
##Script is to compare times between Portland, New York, and London,
##to see if New York or London offices are open/closed.  (open 09:30 am - 09:30 pm)
##Portland is given the local time of the user. 

import datetime


PortlandTime = datetime.datetime.now()
PortlandTimeStr = PortlandTime.strftime('%I:%M %p')
#print 'Portland Time', PortlandTime
#print 'PortlandTimeStr', PortlandTimeStr

LondonTimeDiff = datetime.timedelta(hours=8)
LondonTime = (PortlandTime + datetime.timedelta(hours=8)).time()
LondonTimeStr = LondonTime.strftime('%I:%M %p')

NewYorkTimeDiff = datetime.timedelta(hours=3)
NewYorkTime = (PortlandTime + NewYorkTimeDiff).time()
NewYorkTimeStr = NewYorkTime.strftime('%I:%M %p')

#print 'London Time', LondonTimeStr
#print 'New York Time', NewYorkTimeStr

LondonOpen = datetime.datetime.strptime("09:30", "%H:%M").time()
LondonOpenStr = LondonOpen.strftime("%I:%M %p")
LondonClose = datetime.datetime.strptime("21:30", "%H:%M").time()
LondonCloseStr = LondonClose.strftime("%I:%M %p")

NewYorkOpen = datetime.datetime.strptime("09:30", "%H:%M").time()
NewYorkOpenStr = NewYorkOpen.strftime("%I:%M %p")
NewYorkClose = datetime.datetime.strptime("21:30", "%H:%M").time()
NewYorkCloseStr = NewYorkClose.strftime("%I:%M %p")

##print 'portland', PortlandTime
##print 'LondonTime', LondonTime, 'LondonOpen', LondonOpen, 'LondonClose', LondonClose
##print 'NewYorkTime', NewYorkTime, 'NewYorkOpen', NewYorkOpen, 'NewYorkClose', NewYorkClose
##print

print "The current time in Portland is", PortlandTimeStr, "\n"
if LondonTime >= LondonOpen and LondonTime <= LondonClose:
        print "The time in London is", LondonTimeStr
        print "London is open\n"
else:
        print "The time in London is", LondonTimeStr
        print "London is closed\n"

if NewYorkTime >= NewYorkOpen and NewYorkTime <= NewYorkClose:
        print "The time in New York is", NewYorkTimeStr
        print "New York is open"
else:
        print "The time in New York is", NewYorkTimeStr
        print "New York is closed"

##Test of code
##for i in range(24):
##    PortlandTime = datetime.datetime.now()
##    PortlandTime = PortlandTime + datetime.timedelta(hours=i)
##    time_assignment(PortlandTime)

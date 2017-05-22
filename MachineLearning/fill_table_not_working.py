import time
import MySQLdb
from MySQLdb import *
import datetime
import json



date = time.localtime()
# print date
year_mon_date_day = [date.tm_year, date.tm_mon, date.tm_mday, date.tm_wday]
new = '('+str(date.tm_year)+ ','+ str(date.tm_mon)+ ',' + str(date.tm_mday) + ',' + str(date.tm_wday)+')'
# print new

column = ''
if date.tm_hour==10:
    if date.tm_min<=15:
        column = "10:00-10:15"
    elif date.tm_min<=30:
        column = "10:15-10:30"
    elif date.tm_min <= 45:
        column = "10:30-10:45"
    elif date.tm_min <= 60:
        column = "10:45-11:00"

elif date.tm_hour==11:
    if date.tm_min<=15:
        column = "11:00-11:15"
    elif date.tm_min<=30:
        column = "11:15-11:30"
    elif date.tm_min <= 45:
        column = "11:30-11:45"
    elif date.tm_min <= 60:
        column = "11:45-12:00"

elif date.tm_hour==12:
    if date.tm_min<=15:
        column = "12:00-12:15"
    elif date.tm_min<=30:
        column = "12:15-12:30"
    elif date.tm_min <= 45:
        column = "12:30-12:45"
    elif date.tm_min <= 60:
        column = "12:45-01:00"

elif date.tm_hour==13:
    if date.tm_min<=15:
        column = "01:00-01:15"
    elif date.tm_min<=30:
        column = "01:15-01:30"
    elif date.tm_min <= 45:
        column = "01:30-01:45"
    elif date.tm_min <= 60:
        column = "01:45-02:00"

elif date.tm_hour==16:
    if date.tm_min<=15:
        column = "02:00-02:15"
    elif date.tm_min<=30:
        column = "02:15-02:30"
    elif date.tm_min <= 45:
        column = "02:30-02:45"
    elif date.tm_min <= 60:
        column = "02:45-03:00"
else:
    pass


db = MySQLdb.connect(host='localhost', user='root', passwd='8192',db='traffic_record')
cursor=db.cursor()


if column == "10:00-10:15":
        query = '''INSERT INTO `traffic_record`.`RoadA` ( `Date`,`Day`,`''' + column + '''`) VALUES ('%s','%s','%s')'''
        print year_mon_date_day
        value = (year_mon_date_day, date.tm_wday, 9)
        print value
else:
        print column
        query = '''UPDATE RoadA set Day=%s WHERE Id=%s'''
        value = (3,1)

# print query
cursor.execute(query, value)

db.commit()
db.close()

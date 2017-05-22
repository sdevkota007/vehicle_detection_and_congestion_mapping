import time
import MySQLdb
from MySQLdb import *
import datetime
import random



date = time.localtime()
year_mon_date_day = [date.tm_year, date.tm_mon, date.tm_mday, date.tm_wday]

column=[]
# column = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10]
i=0
while i<16:
    column.append(random.randrange(100,175))
    i+=1


x=10


while (date.tm_hour<=1):
 if date.tm_hour==10:
    if date.tm_min==15:
        column.append(x)
    elif date.tm_min==30:
        column.append(x)
    elif date.tm_min == 45:
        column.append(x)
    elif date.tm_min == 60:
        column.append(x)
    else:
        pass

 elif date.tm_hour==11:
    if date.tm_min==15:
        column.append(x)
    elif date.tm_min==30:
        column.append(x)
    elif date.tm_min == 45:
        column.append(x)
    elif date.tm_min == 60:
        column.append(x)
    else:
        pass

 elif date.tm_hour==12:
    if date.tm_min==15:
        column.append(x)
    elif date.tm_min==30:
        column.append(x)
    elif date.tm_min == 45:
        column.append(x)
    elif date.tm_min == 60:
        column.append(x)
    else:
        pass

 elif date.tm_hour==13:
    if date.tm_min==15:
        column.append(x)
    elif date.tm_min==30:
        column.append(x)
    elif date.tm_min== 45:
        column.append(x)
    elif date.tm_min== 60:
        column.append(x)
    else:
        pass

 elif date.tm_hour==14:
    if date.tm_min==15:
        column.append(x)
    elif date.tm_min==30:
        column.append(x)
    elif date.tm_min == 45:
        column.append(x)
    elif date.tm_min == 60:
        column.append(x)
    else:
        pass
 else:
    pass


db = MySQLdb.connect(host='localhost', user='root', passwd='2864',db='traffic_record')
cursor =db.cursor()

print column
query = '''INSERT INTO `traffic_record`.`RoadC` ( `Date`,`Day`,`10:00-10:15`,`10:15-10:30`,`10:30-10:45`,`10:45-11:00`,`11:00-11:15`,`11:15-11:30`,`11:30-11:45`,`11:45-12:00`,`12:00-12:15`,`12:15-12:30`,`12:30-12:45`,`12:45-01:00`,`01:00-01:15`,`01:15-01:30`,`01:30-01:45`,`01:45-02:00`) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')'''
value = (year_mon_date_day, date.tm_wday, column[0],column[1],column[2],column[3],column[4],column[5],column[6],column[7],column[8],column[9],column[10],column[11],column[12],column[13],column[14],column[15])
print value
cursor.execute(query, value)

db.commit()
db.close()

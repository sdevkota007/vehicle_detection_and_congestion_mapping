import time
import MySQLdb
import csv
import numpy as np
import pandas as pd
# import sklearn



db = MySQLdb.connect(host='localhost', user='root', passwd='2864',db='traffic_record')
cursor=db.cursor()

date=time.localtime()


sql = '''SELECT * from `RoadA` where Day=%s'''
value = (date.tm_wday,)
cursor.execute(sql , value)
rows=cursor.fetchall()

df = pd.DataFrame(columns = ['Id','Day','10:00-10:15', '10:15-10:30', '10:30-10:45', '10:45-11:00', '11:00-11:15', '11:15-11:30', '11:30-11:45', '11:45-12:00', '12:00-12:15', '12:15-12:30', '12:30-12:45', '12:45-01:00', '01:00-01:15', '01:15-01:30', '01:30-01:45', '01:45-02:00', '02:00-02:15', '02:15-02:30', '02:30-01:45', '02:45-03:00'])

try:
    i=0
    while(1):
        # print (rows[i])
        c=rows[i]
        df = df.append({'Id':i,'Day':c[2], '10:00-10:15':c[3], '10:15-10:30':c[4], '10:30-10:45':c[5], '10:45-11:00':c[6], '11:00-11:15':c[7],
                       '11:15-11:30':c[8], '11:30-11:45':c[9], '11:45-12:00':c[10], '12:00-12:15':c[11], '12:15-12:30':c[12], '12:30-12:45':c[13],
                       '12:45-01:00':c[14], '01:00-01:15':c[15], '01:15-01:30':c[16], '01:30-01:45':c[17], '01:45-02:00':c[18], '02:00-02:15':c[19],
                       '02:15-02:30':c[20], '02:30-01:45':c[21], '02:45-03:00':c[22]}, ignore_index = True)
        i+=1

except:
    print('No more rows')
df.to_csv('out.csv')
db.commit()
db.close()
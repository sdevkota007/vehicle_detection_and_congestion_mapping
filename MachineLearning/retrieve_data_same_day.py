import time
import MySQLdb
import csv
import numpy
import sklearn


db = MySQLdb.connect(host='localhost', user='root', passwd='2864',db='traffic_record')
cursor=db.cursor()

date=time.localtime()


sql = '''SELECT * from `Road A` where Day=%s'''
value = (date.tm_wday,)
cursor.execute(sql , value)
rows=cursor.fetchall()

# Incase CSV file is needed for machine learning

# with open("out.csv", "wb") as csv_file:
#     csv_writer = csv.writer(csv_file)
#     csv_writer.writerow([i[0] for i in cursor.description])  # write headers
#     csv_writer.writerows(cursor)



try:
    i=0
    while(1):
        print (rows[i])
        c=rows[i]
        j=3
        while (j<=5):
            print c[j]
            j+=1
        i+=1

except:
    print('No more rows')

db.commit()
db.close()
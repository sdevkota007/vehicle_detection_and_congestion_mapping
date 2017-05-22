import time
import MySQLdb
import exceptions

def test_func(x):
    date = time.localtime()
    # print date
    year_mon_date_day = [date.tm_year, date.tm_mon, date.tm_mday, date.tm_wday]
    new = '('+str(date.tm_year)+ ','+ str(date.tm_mon)+ ',' + str(date.tm_mday) + ',' + str(date.tm_wday)+')'
    query = ''
    if date.tm_hour==10:
        if date.tm_min==15:
            query = '''INSERT INTO `traffic_record`.`RoadA` ( `Date`,`Day`,`10:00-10:15`) VALUES ('%s','%s','%s')'''
        elif date.tm_min==30:
            query = '''UPDATE RoadA set `10:15-10:30`=%s WHERE Id=%s'''
        elif date.tm_min == 45:
            query = '''UPDATE RoadA set `10:30-10:45`=%s WHERE Id=%s'''
        else:
            pass

    elif date.tm_hour==11:
        if date.tm_min == 00:
            query = '''UPDATE RoadA set `10:45-11:00`=%s WHERE Id=%s'''
        elif date.tm_min==15:
            query = '''UPDATE RoadA set `11:00-11:15`=%s WHERE Id=%s'''
        elif date.tm_min==30:
            query = '''UPDATE RoadA set `11:15-11:30`=%s WHERE Id=%s'''
        elif date.tm_min == 45:
            query = '''UPDATE RoadA set `11:30-11:45`=%s WHERE Id=%s'''
        else:
            pass

    elif date.tm_hour==12:
        if date.tm_min == 00:
            query = '''UPDATE RoadA set `11:45-12:00`=%s WHERE Id=%s'''
        elif date.tm_min==15:
            query = '''UPDATE RoadA set `12:00-12:15`=%s WHERE Id=%s'''
        elif date.tm_min==30:
            query = '''UPDATE RoadA set `12:15-12:30`=%s WHERE Id=%s'''
        elif date.tm_min == 45:
            query = '''UPDATE RoadA set `12:30-12:45`=%s WHERE Id=%s'''
        else:
            pass

    elif date.tm_hour==13:
        if date.tm_min == 00:
            query = '''UPDATE RoadA set `12:45-01:00`=%s WHERE Id=%s'''
        elif date.tm_min==15:
            query = '''UPDATE RoadA set `01:00-01:15`=%s WHERE Id=%s'''
        elif date.tm_min==30:
            query = '''UPDATE RoadA set `01:15-01:30`=%s WHERE Id=%s'''
        elif date.tm_min == 45:
            query = '''UPDATE RoadA set `01:30-01:45`=%s WHERE Id=%s'''
        else:
            pass


    elif date.tm_hour==14:
        if date.tm_min == 00:
            query = '''UPDATE RoadA set `01:45-02:00`=%s WHERE Id=%s'''
        else:
            pass

    else:
        pass


    db = MySQLdb.connect(host='localhost', user='root', passwd='2864',db='traffic_record')
    cursor=db.cursor()

    if date.tm_hour==10 and date.tm_min==15:
            value = (year_mon_date_day, date.tm_wday, x)

    elif (date.tm_min==15 or date.tm_min==30 or date.tm_min==45 or date.tm_min==00) and (date.tm_hour==10 or date.tm_hour==11 or
                                                                                                date.tm_hour==12 or
                                                                                               date.tm_hour==13 or
                                                                                               date.tm_hour==14):
            sql = '''SELECT * from `RoadA` where Date=%s'''
            value = (new,)
            cursor.execute(sql, value)
            rows = cursor.fetchall()        #get data of all day
            i = rows[0]                     #get current date data
            value = (x,i[0],)               #x is the number of vehicles during that time frame
            print value
    else:
        pass

    print query

    try:
        cursor.execute(query, value)
    except exceptions as e:
        print (e)
    finally:
        db.commit()
        db.close()

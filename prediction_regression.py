import math
import numpy as np
import pandas as pd
from sklearn import cross_validation, svm, preprocessing
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import datetime
import pickle
import time
import csv



def regression_prediction(x,feature_var,forecast_var):
    df = pd.read_csv(x)
    # print feature_var, forecast_var

    df = df[[feature_var,forecast_var]]
    # print df.tail()

    forecast_col = forecast_var
    df.fillna(value=-99999, inplace=True)
    forecast_out = int(math.ceil(0.01 * len(df)))

    df['label'] = df[forecast_col].shift(-forecast_out)

    X = np.array(df.drop(['label'], 1))
    # X = preprocessing.scale(X)
    X_lately = X[-forecast_out:]
    X = X[:-forecast_out]

    df.dropna(inplace=True)

    y = np.array(df['label'])


    X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size=0.4)
    #COMMENTED OUT:
    clf = svm.SVR(kernel='linear')
    clf.fit(X_train, y_train)
    confidence = clf.score(X_test, y_test)
    print(confidence)
    # pickle_in = open('linearregression.pickle','rb')
    # clf = pickle.load(pickle_in)

    forecast_set = clf.predict(X_lately)
    df['Forecast'] = np.nan
    last_id = df.iloc[-1].name+1
    print last_id
    next_id = last_id




    for i in forecast_set:
        df.loc[next_id]=[np.nan for _ in range(len(df.columns)-1)]+[i]
        print df.tail()
        print df[feature_var]
        return (df['Forecast'].loc[next_id])
        next_id+=1

def passing_value():
    feature_var = None
    forecast_var = None
    date = time.localtime()
    if (date.tm_min == 00 and date.tm_hour==10):
        feature_var = "Id"
        forecast_var = "10:00-10:15"
    elif (date.tm_min == 15 and date.tm_hour == 10):
        feature_var = "10:00-10:15"
        forecast_var = "10:15-10:30"

    elif (date.tm_min == 30 and date.tm_hour == 10):
        feature_var = "10:15-10:30"
        forecast_var = "10:30-10:45"

    elif (date.tm_min == 45 and date.tm_hour == 10):
        feature_var = "10:30-10:45"
        forecast_var = "10:45-11:00"

    elif (date.tm_min == 00 and date.tm_hour==11):
        feature_var = "10:45-11:00"
        forecast_var = "11:00-11:15"

    elif (date.tm_min == 15 and date.tm_hour == 11):
        feature_var = "11:00-11:15"
        forecast_var = "11:15-11:30"

    elif (date.tm_min == 30 and date.tm_hour == 11):
        feature_var = "11:15-11:30"
        forecast_var = "11:30-11:45"

    elif (date.tm_min == 45 and date.tm_hour == 11):
        feature_var = "11:30-11:45"
        forecast_var = "11:45-12:00"

    elif (date.tm_min == 00 and date.tm_hour == 12):
        feature_var = "11:45-12:00"
        forecast_var = "12:00-12:15"

    elif (date.tm_min == 15 and date.tm_hour == 12):
        feature_var = "12:00-12:15"
        forecast_var = "12:15-12:30"

    elif (date.tm_min == 30 and date.tm_hour == 12):
        feature_var = "12:15-12:30"
        forecast_var = "12:30-12:45"

    elif (date.tm_min == 45 and date.tm_hour == 12):
        feature_var = "12:30-12:45"
        forecast_var = "12:45-13:00"

    elif (date.tm_min == 00 and date.tm_hour == 13):
        feature_var = "12:45-13:00"
        forecast_var = "01:00-01:15"

    elif (date.tm_min == 15 and date.tm_hour == 13):
        feature_var = "01:00-01:15"
        forecast_var = "01:15-01:30"

    elif (date.tm_min == 30 and date.tm_hour == 13):
        feature_var = "01:15-01:30"
        forecast_var = "01:30-01:45"

    elif (date.tm_min == 45 and date.tm_hour == 13):
        feature_var = "01:30-01:45"
        forecast_var = "01:45-02:00"

    else:
        feature_var = "01:30-01:45"
        forecast_var = "01:45-02:00"


    # print feature_var
    # print forecast_var

    return feature_var, forecast_var


#assign -1, 0 and 1 as value for low, medium and high traffic to all roads
def compare_forecast():
    feature_var,forecast_var = passing_value()
    a = regression_prediction('out1.csv',feature_var,forecast_var)
    if a <120:
        A=-1
    elif a < 140:
        A=0
    else:
        A=1
    b = regression_prediction('out2.csv',feature_var,forecast_var)
    if b < 120:
        B = -1
    elif b < 140:
        B = 0
    else:
        B = 1
    c = regression_prediction('out3.csv',feature_var,forecast_var)
    if c < 120:
        C = -1
    elif c < 140:
        C = 0
    else:
        C = 1
    print a, b, c
    print A, B, C
    cursor = []
    cursor.append(A)
    cursor.append(B)
    cursor.append(C)
    print cursor
    with open("sample.csv", "wb") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(cursor)
    road = returnRoad(A,B,C)
    print road


def returnRoad(a,b,c):
    max=a
    if(b>max):
        max=b
    if(c>max):
        max=c

    # print max
    if (max==a):
        return "RoadA"
    elif (max==b):
        return "RoadB"
    else:
        return "RoadC"

Choice = compare_forecast()
# print Choice

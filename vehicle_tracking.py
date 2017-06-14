import cv2
import numpy as np
from operator import itemgetter

# CENTROID_DIFFERENCE = 60
# THRESHOLD_OF_HISTOGRAM = 0.4





def isCentroidNear(car1_arr,  car2_arr, CENTROID_DIFFERENCE_THRESH):
    x,y,w,h = car1_arr
    car1_centroidx = x+(w/2)
    car1_centroidy = y+(h/2)
    xp,yp,wp,hp = car2_arr
    car2_centroidx = xp+(wp/2)
    car2_centroidy = yp+(hp/2)

    if abs(car1_centroidx-car2_centroidx)<CENTROID_DIFFERENCE_THRESH/1.5 and abs(car1_centroidy-car2_centroidy)<CENTROID_DIFFERENCE_THRESH:
        return True
    else:
        return False


def featureMatch(roi_newcar, roi_presentcar):
    img1 = roi_newcar
    img2 = roi_presentcar
    print 'img1: ',img1
    print 'img2: ',img2
    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    orb = cv2.ORB_create()
    print orb, type(orb)

    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    if len(matches)>50:
        return True
    else:
        return False


def compareHist(img1, img2, THRESHOLD_OF_HISTOGRAM):
    hist_img1 = calculateHist(img1)
    hist_img2 = calculateHist(img2)
    doc = cv2.compareHist(hist_img1, hist_img2, cv2.HISTCMP_CORREL)
    # doc:degree of correlation
    if doc>THRESHOLD_OF_HISTOGRAM:
        return True
    else:
        return False



def calculateHist(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hist = cv2.calcHist(img, [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
    hist = cv2.normalize(hist, hist, 0, 255, cv2.NORM_MINMAX)
    return hist.flatten()

def removeFalsePositives(cars, LOWER_LIMIT = None, UPPER_LIMIT = None):
    temp = []

    a = 0
    if LOWER_LIMIT!=None and UPPER_LIMIT == None:
        for (x, y, w, h) in cars:
            if w >= LOWER_LIMIT and h >= LOWER_LIMIT:
                temp.append(cars[a])
            a = a + 1
    elif UPPER_LIMIT!=None and LOWER_LIMIT == None:
        for (x, y, w, h) in cars:
            if w <= UPPER_LIMIT and h <= UPPER_LIMIT:
                temp.append(cars[a])
            a = a + 1

    elif LOWER_LIMIT!=None and UPPER_LIMIT!=None :
        for (x, y, w, h) in cars:
            if (LOWER_LIMIT <= w <= UPPER_LIMIT) and (LOWER_LIMIT <= h <= UPPER_LIMIT):
                temp.append(cars[a])
            a = a + 1
    else:
        pass
    # print "temp: ", temp
    return temp


def emptyVehiclesOutOfWindow(some_lst, present_count, last_count):
    if present_count>10 and len(some_lst)>4:
        diff = present_count-last_count
        if str(type(some_lst))!= "<type 'list'>":
            some_lst = some_lst.tolist()

        #sort according to the y-axis
        some_lst = sorted(some_lst, key=itemgetter(1), reverse=True)
        [some_lst.remove(some_lst[0]) for i in range (0,diff) if diff>0]
        return np.array(some_lst)
    else:
        return some_lst

def padding(arr):
    if len(arr)!=0:
        some_lst = []
        for x,y,w,h in arr:
            pad_w, pad_h = int(0.45*w), int(0.45*h)
            # some_lst.append([int(x+1.5*pad_w), int(y+1.5*pad_h), w-pad_w, h-pad_h])
            some_lst.append([int(x+0.5*pad_w), int(y+0.5*pad_h), w-pad_w, h-pad_h])

        return np.array(some_lst)
    else:
        return arr
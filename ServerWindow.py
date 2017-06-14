# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ServerWindow.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
e
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys
import os
import temp


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_serverWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.c_count = 0
        self.b_count = 0
        self.setupUi(self)


    def setupUi(self, serverWindow):
        serverWindow.setObjectName(_fromUtf8("serverWindow"))
        serverWindow.resize(405, 377)
        self.centralwidget = QtGui.QWidget(serverWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.startButton = QtGui.QPushButton(self.centralwidget)
        self.startButton.setGeometry(QtCore.QRect(20, 170, 101, 27))
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.label_bike = QtGui.QLabel(self.centralwidget)
        self.label_bike.setGeometry(QtCore.QRect(20, 250, 151, 17))
        self.label_bike.setObjectName(_fromUtf8("label_bike"))
        self.label_car = QtGui.QLabel(self.centralwidget)
        self.label_car.setGeometry(QtCore.QRect(20, 220, 151, 17))
        self.label_car.setObjectName(_fromUtf8("label_car"))
        self.carCount = QtGui.QLabel(self.centralwidget)
        self.carCount.setGeometry(QtCore.QRect(170, 220, 68, 17))
        self.bikeCount = QtGui.QLabel(self.centralwidget)
        self.bikeCount.setGeometry(QtCore.QRect(170, 250, 68, 17))
        self.carCount.setObjectName(_fromUtf8("carCount"))
        self.bikeCount.setObjectName(_fromUtf8("bikeCount"))
        self.timeLabel = QtGui.QLabel(self.centralwidget)
        self.timeLabel.setGeometry(QtCore.QRect(280, 60, 111, 17))
        self.timeLabel.setObjectName(_fromUtf8("timeLabel"))
        self.systemTime = QtGui.QLabel(self.centralwidget)
        self.systemTime.setGeometry(QtCore.QRect(280, 80, 81, 17))
        self.systemTime.setObjectName(_fromUtf8("systemTime"))
        self.title = QtGui.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(20, 10, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.title.setFont(font)
        self.title.setObjectName(_fromUtf8("title"))
        self.endButton = QtGui.QPushButton(self.centralwidget)
        self.endButton.setGeometry(QtCore.QRect(290, 300, 101, 27))
        self.endButton.setObjectName(_fromUtf8("endButton"))
        serverWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(serverWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 405, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        serverWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(serverWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        serverWindow.setStatusBar(self.statusbar)
        self.retranslateUi(serverWindow)
        QtCore.QMetaObject.connectSlotsByName(serverWindow)
        # self.startButton.clicked['bool'].connect(temp.mainfunc())
        self.connect(self.startButton,SIGNAL("clicked()"),self.mainfunc)
        self.connect(self.endButton,SIGNAL("clicked()"),exit)
        self.carCount.setObjectName(_fromUtf8("carCount"))
        self.bikeCount.setObjectName(_fromUtf8("bikeCount"))

    def mainfunc(self):
        import numpy as np
        import cv2
        import nms
        import os
        import vehicle_tracking
        import datetime, time
        # import test_database
        # import prediction_regression
        # import sklearn_test
        # import PyQt4

        update = False


        xc=10
        yc=20
        line1 = [(10,380),(180,20)]
        line2 = [(465,20),(750,295)]
        drawLines = False

        cars_count=0
        last_cars_count=0

        car_cascade = cv2.CascadeClassifier('haarcascade_nepalese_vehicles.xml')
        cap = cv2.VideoCapture('cctv1.mp4')
        ret, img = cap.read()
        scaling_factor = 0.4
        height=int(np.size(img,0) * scaling_factor)
        width=int(np.size(img,1) * scaling_factor)
        detection_region = [(0, int(0.3*height)), (width, int(0.95 * height))]
        carspresent = []


        bikes_count=0
        last_bikes_count=0
        bikespresent = []
        hog = cv2.HOGDescriptor()
        hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )


        def draw_detections(img, rects, thickness = 1):
            for x, y, w, h in rects:
                # the HOG detector returns slightly larger rectangles than the real objects.
                # so we slightly shrink the rectangles to get a nicer output.
                # pad_w, pad_h = int(0.15*w), int(0.05*h)
                # cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
                pad_w, pad_h = int(0.25*w), int(0.25*h)
                cv2.rectangle(img, (int(x+1.5*pad_w), int(y+1.5*pad_h)), (x+w-pad_w, y+h-pad_h), (255, 0, 0), thickness)




        def compareObjects(cars, carspresent, cars_count, CENTROID_DIFFERENCE_THRESH, THRESHOLD_OF_HISTOGRAM):

            # if there are no cars present in the frame, then there is no point in executing any of these statements
            if len(cars) != 0:
                # roi_cars is the array of regions of interest of all the cars present in the current frame
                roi_cars = []
                roi_carspresent = []

                for (x, y, w, h) in cars:
                    roi_cars.append(img[y:y + h, x:x + w])

                if len(carspresent) == 0:
                    carspresent = cars
                    roi_carspresent = roi_cars
                else:
                    for (x, y, w, h) in carspresent:
                        roi_carspresent.append(img[y:y + h, x:x + w])

                # declaration of some temporary variables to make it easier for executing the for loops
                carspresent_temp = carspresent
                cars_temp = cars
                roi_carspresent_temp = roi_carspresent
                roi_cars_temp = roi_cars


                # for every car 'A' present in the 'carspresent' array,ie of previous frame,
                # 'A' is compared with every other car,'B', in the 'cars' array,ie  of current frame.
                # If there is some degree of similarity between A and B, car A is replaced by b,
                # If there is no similarity at all, B must be a new car, so it is added to the array carspresent
                # and count is incremeted .
                for i in range(0, len(cars_temp)):
                    newcar = cars_temp[i]
                    roi_newcar = roi_cars_temp[i]
                    update = False
                    for j in range(0, len(carspresent_temp)):
                        roi_presentcar = roi_carspresent_temp[j]
                        presentcar = carspresent_temp[j]
                        if vehicle_tracking.isCentroidNear(newcar,presentcar, CENTROID_DIFFERENCE_THRESH = CENTROID_DIFFERENCE_THRESH):
                             # and vehicle_tracking.compareHist(roi_newcar, roi_presentcar, THRESHOLD_OF_HISTOGRAM = THRESHOLD_OF_HISTOGRAM):
                            update = True
                            carspresent[j] = cars[i]
                            roi_carspresent[j] = roi_cars[i]
                    if update == False:
                        carspresent = np.vstack((carspresent, cars[i]))
                        cars_count = cars_count+1
                        roi_carspresent.append(roi_cars[i])

            return carspresent, cars_count




        while 1:
            date = time.localtime()
            ret, img = cap.read()
            img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            #***********************************************************************************************************************************************************
            # cars_without_nms may contain overlaping bounding boxes,
            # the non maximum supression removes all the overlapping bounding boxes,
            # overlapThresh is the threshold, for more info visit pyimagesearch.com
            cars_without_nms = car_cascade.detectMultiScale(gray, 6, 5)
            cars = nms.non_max_suppression_fast(cars_without_nms, overlapThresh=0.1)

            #---------------------------------------------------------------------------------------------------------------------
            # removal of false positives and filtering out those cars outside of the detection region
            cars_inside_box = []
            if len(cars)!=0:
                # cars, which is a numpy array is changed to a list before removing false positives,
                # after removing the false positives, the result is changed back to numpy array
                cars = vehicle_tracking.removeFalsePositives(cars.tolist(),LOWER_LIMIT=41, UPPER_LIMIT= 200)
                cars = np.array(cars)


                i = 0
                for (x, y, w, h) in cars:
                    if y > detection_region[0][1] and y + h < detection_region[1][1]:
                        cars_inside_box.append(cars[i].tolist())
                    i = i + 1
            cars_inside_box = np.array(cars_inside_box)

            #---------------------------------------------------------------------------------------------------------------------


            # the function compareObject compares all the objects detected in this frame with cars present from the previous frame
            # if new objects have arrived in the frame, it increments the count by the no of new objects that just arrived in the frame.
            carspresent, cars_count = compareObjects(cars_inside_box,carspresent,cars_count, CENTROID_DIFFERENCE_THRESH=50, THRESHOLD_OF_HISTOGRAM=0.6)
            carspresent = nms.non_max_suppression_fast(carspresent, 0.9999999)
            # emptyVehiclesOutOfWindow function removes the bounding boxes
            # of those vehicles that have possibly gone out of the window(detection region)
            carspresent = vehicle_tracking.emptyVehiclesOutOfWindow(carspresent, cars_count, last_cars_count)
            last_cars_count = cars_count


            for (x, y, w, h) in cars_inside_box:
                cv2.rectangle(gray, (x, y), (x + w, y + h), (255, 0, 0), 1)

            cv2.putText(gray, 'Four Wheelers= ' + str(cars_count), (0, height), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), thickness=2)






            #***********************************************************************************************************************************************************

            bikes_without_nms, w = hog.detectMultiScale(gray, winStride=(8, 8), padding=(16, 16), scale=1.25)

            # bikes_without_nms may contain overlaping bounding boxes,
            # the non maximum supression removes all the overlapping bounding boxes,
            # overlapThresh is the threshold, for more info visit pyimagesearch.com
            bikes = nms.non_max_suppression_fast(bikes_without_nms, overlapThresh=0.8)

            # ---------------------------------------------------------------------------------------------------------------------
            # removal of false positives and filtering out those bikes outside of the detection region
            bikes_inside_box = []
            if len(bikes) != 0:
                # bikes, which is a numpy array is changed to a list before removing false positives,
                # after removing the false positives, the result is changed back to numpy array
                print "bikes before: ", bikes
                bikes = vehicle_tracking.removeFalsePositives(bikes.tolist(), UPPER_LIMIT=400)
                bikes = np.array(bikes)
                print "bikes after: ", bikes

                i = 0
                for (x, y, w, h) in bikes:
                    if y > detection_region[0][1] and y + h < detection_region[1][1]:
                        bikes_inside_box.append(bikes[i].tolist())
                    i = i + 1
            bikes_inside_box = np.array(bikes_inside_box)

            # ---------------------------------------------------------------------------------------------------------------------


            # the function compareObject compares all the objects detected in this frame with bikes present from the previous frame
            # if new objects have arrived in the frame, it increments the count by the no of new objects that just arrived in the frame.
            bikespresent, bikes_count = compareObjects(bikes_inside_box, bikespresent, bikes_count,
                                                       CENTROID_DIFFERENCE_THRESH=45, THRESHOLD_OF_HISTOGRAM=0.5)
            bikespresent = nms.non_max_suppression_fast(bikespresent, 0.9999999)
            # emptyVehiclesOutOfWindow function removes the bounding boxes
            # of those vehicles that have possibly gone out of the window(detection region)
            bikespresent = vehicle_tracking.emptyVehiclesOutOfWindow(bikespresent, bikes_count, last_bikes_count)
            last_bikes_count = bikes_count

            # print "bikes_inside_box: \n", bikes_inside_box
            # print "bikes_present: \n", bikespresent


            # draw_detections(gray,bikes_inside_box)
            draw_detections(gray, bikes_inside_box)

            cv2.putText(gray, 'Two Wheelers= ' + str(bikes_count), (int(width/2), height), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), thickness=2)
            cv2.rectangle(gray, detection_region[0], detection_region[1], (255, 255, 0), thickness=2)



            #***********************************************************************************************************************************************************








            cv2.rectangle(gray, detection_region[0], detection_region[1], (0, 0, 255))

            cv2.circle(gray, (xc, yc), 1, (255, 0, 0), thickness=3)
            if drawLines:
                cv2.line(gray, line1[0], line1[1], (255, 0, 0))
                cv2.line(gray, line2[0], line2[1], (255, 0, 0))
            cv2.imshow("main window", gray)

            # print xc,yc
            k = cv2.waitKey(15) & 0xff
            if k == 27:
                break
            elif k == 119:
                yc = yc - 5
            elif k == 97:
                xc = xc - 5
            elif k == 115:
                yc = yc + 5
            elif k == 100:
                xc = xc + 5
            elif k == 49:
                line1.append((xc, yc))
                print 'Line 1, starting point set to: ', line1[0]
            elif k == 50:
                line1.append((xc, yc))
                print 'Line 1, ending point set to: ', line1[1]
            elif k == 51:
                line2.append((xc, yc))
                print 'Line 2, starting point set to: ', line2[0]
            elif k == 52:
                line2.append((xc, yc))
                print 'Line 2, ending point set to: ', line2[1]
            elif k == 32:
                drawLines = True

            # print date.tm_min
            # if (date.tm_min == 15 or date.tm_min == 30 or date.tm_min == 45 or date.tm_min == 00) and update==False:
            #     update = True
            #     test_database.test_func(cars_count+bikes_count)
            #     sklearn_test.sklearn_func()
            #     # Choice = prediction_regression.compare_forecast()
            #     cars_count=0
            #     bikes_count=0


            # cv2.waitKey(0)
            print"-----------------------------------------------------------------------------"
            self.c_count = cars_count
            self.b_count = bikes_count
            self.carCount.setText(_translate("serverWindow", str(self.c_count), None))
            self.bikeCount.setText(_translate("serverWindow", str(self.b_count), None))
            self.systemTime.setText(_translate("serverWindow", str(date.tm_hour)+":"+str(date.tm_min), None))


        cap.release()
        cv2.destroyAllWindows()






    def retranslateUi(self, serverWindow):
        serverWindow.setWindowTitle(_translate("serverWindow", "MainWindow", None))
        self.startButton.setText(_translate("serverWindow", "Start Process", None))
        self.label_bike.setText(_translate("serverWindow", "No of two wheelers : ", None))
        self.label_car.setText(_translate("serverWindow", "No of four wheelers : ", None))
        self.carCount.setText(_translate("serverWindow", str(self.c_count), None))
        self.bikeCount.setText(_translate("serverWindow", str(self.b_count), None))
        self.timeLabel.setText(_translate("serverWindow", "Time of Day :", None))
        self.systemTime.setText(_translate("serverWindow", "12 : 00 AM", None))
        self.title.setText(_translate("serverWindow", "Vehicle Traffic Detection and Counting", None))
        self.endButton.setText(_translate("serverWindow", "End Process", None))

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    mainWindow = Ui_serverWindow()
    mainWindow.show()
    sys.exit(app.exec_())
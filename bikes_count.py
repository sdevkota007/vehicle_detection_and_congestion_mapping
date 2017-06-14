import numpy as np
import cv2
import numpy as np
import nms
import vehicle_tracking


bikes_count=0
last_bikes_count=0
bikespresent = []

hog = cv2.HOGDescriptor()
hog.setSVMDetector( cv2.HOGDescriptor_getDefaultPeopleDetector() )
cap=cv2.VideoCapture("cctv1.mp4")
ret, img = cap.read()

scaling_factor = 0.4
height=int(np.size(img,0) * scaling_factor)
width=int(np.size(img,1) * scaling_factor)
detection_region = [(0, int(0.3*height)), (width, int(1.0 * height))]



def draw_detections(img, rects, thickness = 1):
    for x, y, w, h in rects:
        # the HOG detector returns slightly larger rectangles than the real objects.
        # so we slightly shrink the rectangles to get a nicer output.
        # pad_w, pad_h = int(0.15*w), int(0.05*h)
        # cv2.rectangle(img, (x+pad_w, y+pad_h), (x+w-pad_w, y+h-pad_h), (0, 255, 0), thickness)
        pad_w, pad_h = int(0.25*w), int(0.25*h)
        # cv2.rectangle(img, (int(x+1.5*pad_w), int(y+1.5*pad_h)), (x+w-pad_w, y+h-pad_h), (255, 0, 0), thickness)
        cv2.rectangle(img, (int(x), int(y)), (x+w, y+h), (255, 0, 0), thickness)



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




while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    bikes_without_nms,w=hog.detectMultiScale(gray, winStride=(8,8), padding=(16,16), scale=1.35)



    # bikes_without_nms may contain overlaping bounding boxes,
    # the non maximum supression removes all the overlapping bounding boxes,
    # overlapThresh is the threshold, for more info visit pyimagesearch.com
    bikes = nms.non_max_suppression_fast(bikes_without_nms, overlapThresh=0.8)
    bikes = vehicle_tracking.padding(bikes)

    #---------------------------------------------------------------------------------------------------------------------
    # removal of false positives and filtering out those bikes outside of the detection region
    bikes_inside_box = []
    if len(bikes)!=0:
        # bikes, which is a numpy array is changed to a list before removing false positives,
        # after removing the false positives, the result is changed back to numpy array
        print "bikes before: ",bikes
        bikes = vehicle_tracking.removeFalsePositives(bikes.tolist(), UPPER_LIMIT= 150)
        bikes = np.array(bikes)
        print "bikes after: ",bikes

        i = 0
        for (x, y, w, h) in bikes:
            if y > detection_region[0][1] and y + h < detection_region[1][1]:
                bikes_inside_box.append(bikes[i].tolist())
            i = i + 1
    bikes_inside_box = np.array(bikes_inside_box)

    #---------------------------------------------------------------------------------------------------------------------


    # the function compareObject compares all the objects detected in this frame with bikes present from the previous frame
    # if new objects have arrived in the frame, it increments the count by the no of new objects that just arrived in the frame.
    bikespresent, bikes_count = compareObjects(bikes_inside_box,bikespresent,bikes_count, CENTROID_DIFFERENCE_THRESH=45, THRESHOLD_OF_HISTOGRAM=0.5)
    bikespresent = nms.non_max_suppression_fast(bikespresent, 0.9999999)
    # emptyVehiclesOutOfWindow function removes the bounding boxes
    # of those vehicles that have possibly gone out of the window(detection region)
    # bikespresent = vehicle_tracking.emptyVehiclesOutOfWindow(bikespresent, bikes_count, last_bikes_count)
    last_bikes_count=bikes_count


    # print "bikes_inside_box: \n", bikes_inside_box
    # print "bikes_present: \n", bikespresent


    # draw_detections(gray,bikes_inside_box)
    draw_detections(gray,bikespresent)

    cv2.putText(gray, 'total bikes= ' + str(bikes_count), (0, height), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255))
    cv2.rectangle(gray, detection_region[0], detection_region[1], (0, 0, 255))
    cv2.rectangle(gray, (10,10), (int(45/1.5),150), (255,0,0),1)

    cv2.imshow("gray", gray)

    # print xc,yc
    k = cv2.waitKey(15) & 0xff
    if k == 27:
        break
    #cv2.waitKey(0)
    print"-----------------------------------------------------------------------------"

cap.release()
cv2.destroyAllWindows()
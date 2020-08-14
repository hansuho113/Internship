# reference
# https://bong-sik.tistory.com/16
# https://go-programming.tistory.com/159


import cv2
import numpy as np
from yolo_classes import classes

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0,255, size=(len(classes),3))

img = cv2.imread("ImageFile/fire_2.jpg")
# img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channles = img.shape

blob = cv2.dnn.blobFromImage(img, 0.00392, (608, 608), (0, 0, 0), True, crop=False)
# cv2.dnn.blobFromImage(image, scalefactor, size, mean, swapRB '')
# blob is used to extract feature from the image and to resize them. (320*320, 609*609, 416*416)
# scale factor : After we perform mean subtraction we can optionally scale our images by some factor ; default(1.0)
# mean : 3-tuple in '(R,G,B)', especially when utilizing the default behavior of swapRB=True
# document : https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
net.setInput(blob)
outs = net.forward(output_layers)

class_ids = []
confidences = []
boxes = []
for out in outs:
    for detection in out:
        scores = detection[5:]
        class_id = np.argmax(scores)
        confidence = scores[class_id]

        if confidence > 0.1:
            center_x = int(detection[0] * width)
            center_y = int(detection[1] * height)
            w = int(detection[2] * width)
            h = int(detection[3] * height)

            x = int(center_x - w / 2)
            y = int(center_y - h / 2)

            boxes.append([x, y, w, h])
            confidences.append(float(confidence))
            class_ids.append(class_id)

indices = cv2.dnn.NMSBoxes(boxes, confidences, 0.4, 0.4)

font = cv2.FONT_HERSHEY_PLAIN
for i in range(len(boxes)):
    if i in indices:
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        color = colors[i]
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

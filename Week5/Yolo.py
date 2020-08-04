# reference
# https://bong-sik.tistory.com/16
# https://go-programming.tistory.com/159



import cv2
import numpy as np
from yolo_classes import classes

net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

img = cv2.imread("ImageFile/dressroom.jpg")
img = cv2.resize(img, None, fx=0.4, fy=0.4)
height, width, channles = img.shape

blob = cv2.dnn.blobFromImage(img, 0.00392, (608, 608), (0, 0, 0), True, crop=False)
net.setInput(blob)
outs = net.forward(output_layers)

class_ids = []
confidence = []
boxes = []
for out in outs:
    for detection in out:
        print(detection[:5])
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

            boxes.append([x,y,w,h])
            confidence.append(float(confidence))
            class_ids.append(class_id)

indices = cv2.dnn.NMSBoxes(boxes, confidence, 0.4, 0.4)
print(indices)



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

# frame = cv2.imread(dressroom)
# color = np.random.uniform(0, 255, size=(len(classes), 3))
#
# height, width, channels = frame.shape
#
# blob = cv2.dnn.blobFromImage(frame, 0.00392, (608, 608), (0, 0, 0), True, crop=False)
# # cv2.dnn.blobFromImage(image, scalefactor, size, mean, swapRB '')
# # scalefactor : After we perform mean subtraction we can optionally scale our images by some factor ; default(1.0)
# # mean : 3-tuple in '(R,G,B)', especially when utilizing the default behavior of swapRB=True
# # document : https://www.pyimagesearch.com/2017/11/06/deep-learning-opencvs-blobfromimage-works/
#
# net.setInput(blob)
#
# outs = net.forward(output_layers)
#
#
# class_ids = []
# confidence = []
# boxes = []
#
# for out in outs:
#     for detection in out:
#         scores = detection[5:]
#         class_id = np.argmax(scores)
#         confidence = scores[class_id]
#
#         if confidence > 0.1:
#             center_x = int(detection[0] * width)
#             center_y = int(detection[1] * height)
#             w = int(detection[2] * width)
#             h = int(detection[3] * height)
#
#             x = int(center_x - w / 2)
#             y = int(center_y - h / 2)
#
#             boxes.append([x,y,w,h])
#             confidence.append(float(confidence))
#             class_ids.append(class_id)
#
# print(f"boxes : {boxes}")
# print(f"confidence: {confidence}")

# score_threshold = 0.4
# nms_threshold = 0.4
# indices = cv2.dnn.NMSBoxes(boxes, confidence, 0.4, 0.4)
#
# print(f"indices : ", end='')
# for index in indices:
#     print(index, end=' ')
# print("\n\n============================== classes ==============================")
#
# for i in range(len(boxes)):
#     if i in indices:
#         x, y, w, h = boxes[i]
#         class_name = classes[class_ids[i]]
#         label = f"{class_name} {confidences[i]:.2f}"
#         color = colors[class_ids[i]]
#
#         # 사각형 테두리 그리기 및 텍스트 쓰기
#         cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
#         cv2.putText(frame, label, (x, y - 8), cv2.FONT_HERSHEY_DUPLEX, 0.7, color, 2)
#
#         # 탐지된 객체의 정보 출력
#         print(f"[{class_name}({i})] conf: {confidences[i]} / x: {x} / y: {y} / width: {w} / height: {h}")
#

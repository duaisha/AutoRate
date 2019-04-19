from imutils import face_utils
from scipy.spatial import distance as dist
import numpy as np
import argparse
import os
import imutils
import dlib
import cv2
import numpy as np
import time

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-p", "--shape-predictor", required=True,
	help="path to facial landmark predictor")
ap.add_argument("-v", "--video", required=True,
	help="path to video image")
args = vars(ap.parse_args())

cap = cv2.VideoCapture(args["video"]);
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(args["shape_predictor"])
i=0

#print(args["video"])
flag =0
while(i<100):
	ret,frame = cap.read()
#	print(frame.shape)
	i +=1
	if (ret == True):
#		print(i)
#		image = cv2.flip(frame,0)
		image = frame	
#		cv2.imshow('frame',image)
#		cv2.waitKey(20)
		#print(image.shape)	
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		rects = detector(gray, 0)
		#print(len(rects))

		if(len(rects) == 0):
			
			continue;
		else:
#			print(i)
			for rect in rects:
				shape = predictor(gray, rect)
				shape = face_utils.shape_to_np(shape)
				(x, y, w, h) = face_utils.rect_to_bb(rect)
#				print(x,y,w,h)
				x1 = (x +w/2)-700
				y1 = 0

				if(x < 0):
					x1 = 0
				else:		
					x1=x

				if(y1 < 0):
					y1 = 0
				x1 =0; y1 =0
				print(x1)
				print(y1)
				flag =1
				break;
#				cv2.rectangle(image,(x1, y1),(x1 +1500,y1+1080),(0,255,0),4)
				#cv2.imwrite('isha.jpg',image)
#				cv2.imshow('frame', image)
#				cv2.waitKey(50)
#			break;
if (flag ==0):
	print("########################################", args["video"],"#################################################")
#	os.remove(args["video"])

cap.release()
cv2.destroyAllWindows()

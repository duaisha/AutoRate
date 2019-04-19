from imutils import face_utils
from scipy.spatial import distance as dist
import numpy as np
import argparse
import imutils
import dlib
import cv2
import numpy as np
import time
import os 

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to video image")
args = vars(ap.parse_args())

x=[]

#tripname="../hams_dataset3_processed2/class1/trip5-0.mp4"
video = cv2.VideoCapture(args["video"]);
width = video.get(cv2.CAP_PROP_FRAME_WIDTH)   # float
height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)
length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
if(length <50):

	print("############################################",args["video"],"##############################################")
	os.remove(args["video"])
	print( width, height,"{0}".format(fps),length)


video.release();

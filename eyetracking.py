# USAGE
# python eyetracking.py --face cascades/haarcascade_frontalface_default.xml --eye cascades/haarcascade_eye.xml

# import the necessary packages
from pyimagesearch.eyetracker import EyeTracker
from pyimagesearch import imutils
import cv2



face = "C:\Users\darre\Documents\python\self_indicating\cascades\haarcascade_frontalface_default.xml"
eye = "C:\Users\darre\Documents\python\self_indicating\cascades/haarcascade_eye.xml"

width = 800

# construct the eye tracker
et = EyeTracker(face, eye)

# if a video path was not supplied, grab the reference
# to the gray
camera = cv2.VideoCapture(0)


# keep looping
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()

	# resize the frame and convert it to grayscale
	frame = imutils.resize(frame, width)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	# detect faces and eyes in the image
	rects = et.track(gray)

	# loop over the face bounding boxes and draw them
	for rect in rects:
		cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (0, 255, 0), 2)

		#print rect[0] # x aixs, left eye
		#print rect[1] # y axis, right eye
		cv2.line(frame, (width / 2, 0), (width / 2, 800), (250, 0, 1), 2) #blue line(crossing line) to be used to check if the eyes crossed line


		if rect[0] > 400:  # x axis left eye
			print "left"
		elif rect[1] < 400: # x axis right eye 
			print "right"

	# show the tracked eyes and face
	cv2.imshow("Tracking", frame)

	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()


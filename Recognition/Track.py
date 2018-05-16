import cv2
import sys

# Each state for the tracking

# Looking for face
CHECKING = 0

# Initialising
INIT  = 1

# Tracking
TRACKING    = 2


# parameters are the frames and the face
def track(frames, userFace):

    # using the median flow tracking algorithm
    tracker = cv2.TrackerMedianFlow_create()
    video = cv2.VideoCapture(0)

    if not video.isOpened():
        print("Could not open video")
        sys.exit()

    TrackingState = 0

    # Region of interest being initialised
    TrackingROI = (0, 0, 0, 0)

    while True:

        # Reading in frames
        ok, frame = video.read()

        # If no frames break
        if not ok:
            break

        # Checking for a face


        elif TrackingState == INIT:

            ok = tracker.init(frame, TrackingROI)
            if ok:
                TrackingState = TRACKING
            else:
                TrackingState = CHECKING

        elif TrackingState == TRACKING:

            ok, TrackingROI = tracker.update(frame)
            if not ok:
                break



        #cv2.imshow("Tracking", frame)

        k = cv2.waitKey(1) & 0xff
        if k == 27: break





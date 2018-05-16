# This project uses the OpenCV library https://github.com/informramiz/opencv-face-recognition-python


import sys
import os
import numpy as np
from camera import Camera
from detect import Detect
import processing as pro
import Track as tr

import cv2

SEARCHING = 0

TRACKING = 1

def get_images(frame, faces_coord):
    faces_img = pro.cut_face_ellipse(frame, faces_coord)
    faces_img = pro.normalize_intensity(faces_img)
    faces_img = pro.resize(faces_img)
    return (frame, faces_img)


def recognize(people_folder):
    try:
        people = [person for person in os.listdir(people_folder)]
    except:
        print "No people in system"
        sys.exit()

    detector = Detect('haarcascade_frontalface_alt.xml')

    recognizer = cv2.face.LBPHFaceRecognizer_create()

    images = []
    labels = []
    labels_people = {}
    for i, person in enumerate(people):
        labels_people[i] = person
        for image in os.listdir(people_folder + person):
            images.append(cv2.imread(people_folder + person + '/' + image, 0))
            labels.append(i)
    try:
        recognizer.train(images, np.array(labels))
    except:
        sys.exit()

    video = Camera()
    getFace(video, detector, recognizer)


def getFace(video, detector, recognizer):
    while True:
        threshold = 70
        frame = video.get_frame()
        face = detector.detect(frame, False)
        if len(face):
            frame, faces_img = get_images(frame, face)
            for i, face_img in enumerate(faces_img):
                pred, Confidence = recognizer.predict(face_img)


                print 'Confidence: ' + str(round(Confidence))
                print 'Threshold: ' + str(threshold)
                if Confidence < threshold:

                    if tr.track(frame, face) == 1:
                        break
                else:
                    cv2.putText(frame, "Unknown",
                                (face[i][0], face[i][1]),
                                cv2.FONT_HERSHEY_PLAIN, 1.7, (206, 0, 209), 2,
                                cv2.LINE_AA)

        cv2.putText(frame, "ESC to exit", (5, frame.shape[0] - 5),
                    cv2.FONT_HERSHEY_PLAIN, 1.2, (206, 0, 209), 2, cv2.LINE_AA)
        #cv2.imshow('Video', frame)
        if cv2.waitKey(100) & 0xFF == 27:
            sys.exit()








if __name__ == '__main__':


    PEOPLE_FOLDER = "C:/Users/daire/Google Drive/College/Year 4/Final Year Project/Project/Facial_Recognition/people/"

    facetracking = 0

    if facetracking == 0:
        recognize(PEOPLE_FOLDER)

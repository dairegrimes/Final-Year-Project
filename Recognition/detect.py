

import cv2


class Detect(object):

    def __init__(self, xml_path):
        # Create classifier object
        self.classifier = cv2.CascadeClassifier(xml_path)

    def detect(self, image, biggest_only=True):

        # converts to grayscale
        is_color = len(image) == 3
        if is_color:
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        else:
            image_gray = image
        # adds the scale
        scale_factor = 1.3

        # puts co-ordinates from the classifier to the variable
        face = self.classifier.detectMultiScale(image_gray,scaleFactor=scale_factor)

        return face





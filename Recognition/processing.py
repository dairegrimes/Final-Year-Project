
import numpy as np
import cv2

# resizes the image so that they are easy to work with

def resize(images, size=(100, 100)):

    images_norm = []
    for image in images:
        is_color = len(image.shape) == 3
        if is_color:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        if image.shape < size:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_AREA)
        else:
            image_norm = cv2.resize(image, size, interpolation=cv2.INTER_CUBIC)
        images_norm.append(image_norm)

    return images_norm

# noramlises the image, this makes the landmarks stand out more
def normalize_intensity(images):
    images_norm = []
    for image in images:
        is_color = len(image.shape) == 3
        if is_color:
            image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        images_norm.append(cv2.equalizeHist(image))
    return images_norm


# cuts face into an ellipse, so there is no background
def cut_face_ellipse(image, face_coord):

    images_ellipse = []
    for (x, y, w, h) in face_coord:
        center = (x + w / 2, y + h / 2)
        axis_major = h / 2
        axis_minor = w / 2
        mask = np.zeros_like(image)

        mask = cv2.ellipse(mask,
                           center=center,
                           axes=(axis_major, axis_minor),
                           angle=0,
                           startAngle=0,
                           endAngle=360,
                           color=(255, 255, 255),
                           thickness=-1)

        image_ellipse = np.bitwise_and(image, mask)
        images_ellipse.append(image_ellipse[y: y + h, x: x + w])

    return images_ellipse


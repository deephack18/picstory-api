import base64
import io
import cv2
from imageio import imread
from matplotlib import pyplot as plt


def compare_images(img1, img2):
    return 17

def compare_images_smart(img1_str, img2_str):
    pass

def base64_str_to_grey_scale(img_str):
    img1 = imread(io.BytesIO(base64.b64decode(img_str)))
    return cv2.cvtColor(img1, cv2.GCV_LOAD_IMAGE_GRAYSCALERE)

def load_grey_scale(path_to_file):
    return cv2.imread('grayscale_image.png', cv2.CV_LOAD_IMAGE_GRAYSCALE)


img1 = load_grey_scale('table.jpeg')
img2 = load_grey_scale('images/LAV039-00950.jpg')



# Initiate SIFT detector
orb = cv2.ORB()

# find the keypoints and descriptors with SIFT
kp1, des1 = orb.detectAndCompute(img1,None)
kp2, des2 = orb.detectAndCompute(img2,None)

# create BFMatcher object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

# Match descriptors.
matches = bf.match(des1,des2)

# Sort them in the order of their distance.
matches = sorted(matches, key = lambda x:x.distance)

# Draw first 10 matches.
img3 = cv2.drawMatches(img1,kp1,img2,kp2,matches[:10], flags=2)

plt.imshow(img3),plt.show()
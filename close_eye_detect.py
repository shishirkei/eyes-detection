import cv2
import os

class EyesDetect:

	def __init__(self):
		self.eyeCascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

	def detect(self, image_path):
		img = cv2.imread(image_path)
		frame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		eyes = self.eyeCascade.detectMultiScale(frame,
							scaleFactor=1.1,
							minNeighbors=5,
							minSize=(30, 30),
							)
		if len(eyes) == 0:
			os.remove(image_path)
			return 'closed'
		else:
			os.remove(image_path)
			return 'opened'

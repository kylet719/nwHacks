from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt
import json

img_path = 'photo-1695927621677-ec96e048dce2.jpeg'
img = cv2.imread(img_path)
plt.imshow(img)

demography = DeepFace.analyze(img_path)
demography = json.loads(json.dumps(demography, default=str))
print(json.dumps(demography, indent=1))
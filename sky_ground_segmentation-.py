import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename
Tk().withdraw()
image_path = askopenfilename(title="tasvir ra entekhab kon", filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
if not image_path:
    raise ValueError("hich file entekhab nashood!")
image = cv2.imread(image_path)
if image is None:
    raise ValueError("tasvir ghabel bargozari nist")
#HSV
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
sky_lower = np.array([90, 30, 60])
sky_upper = np.array([135, 255, 255])
sky_mask = cv2.inRange(hsv, sky_lower, sky_upper)
cloud_lower = np.array([0, 0, 200])
cloud_upper = np.array([180, 60, 255])
cloud_mask = cv2.inRange(hsv, cloud_lower, cloud_upper)
ground_mask = cv2.bitwise_not(sky_mask)
output = image.copy()
output[sky_mask > 0 ] = [255, 200, 0] 
output[ground_mask > 0 ] = [0, 255, 0]    
output[cloud_mask > 0 ] = [255, 255, 255] 
cv2.putText(output, "Sky", (30, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 200), 2)
cv2.putText(output, "Ground", (30, image.shape[0] - 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 0), 2)
cv2.putText(output, "Clouds", (image.shape[1] - 200, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (100, 100, 100), 2)
cv2.imshow("Result", output)
cv2.waitKey(0)
cv2.destroyAllWindows()

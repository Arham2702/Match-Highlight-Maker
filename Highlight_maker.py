import cv2
import pytesseract
import os
import numpy as np
import re
from moviepy.editor import *
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
def Ocr(image):
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
img = cv2.resize(image, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
kernel = np.ones((1, 1), np.uint8)
img = cv2.dilate(img, kernel, iterations=1)
img = cv2.erode(img, kernel, iterations=1)
img_blur = cv2.GaussianBlur(img, (3,3), 0)
options = ""
text = pytesseract.image_to_string(img_blur, cong=options)
result = re.sub('[^0-9]','', text)
print(result)
return result
lst = []
video = 'vid2.mp4'#input("Enter path to the video: ")
dump_path = "Dump"
#input("Enter path to Dump Frame: ")
if ((os.path.isdir(video)) or (os.path.isdir(dump_path))) == False:
print("Invalid Path(s)")
exit()

count = 0
capture = cv2.VideoCapture(video)
while True:
isTrue, frame = capture.read()
if isTrue == False:
print("Frame Capture Done")
break
else:
count += 1
if count%300 == 0 and count > 1200:
cv2.imwrite(dump_path+'/frame_'+str(count)+'.jpg', frame)
cropped_image = frame[45:75, 190:350]
Score = Ocr(cropped_image)
if Score not in lst and Score !="" :
lst.append(Score)
Timestamp = int(oat(str(capture.get(cv2.CAP_PROP_POS_MSEC))) / 1000)
print(f"Time stamp = {Timestamp} sec")
clip = VideoFileClip(video).subclip(Timestamp-20, Timestamp+10)
clip.write_videole(f"vid{Score}_edited.mp4", fps = 30)
print(f"Frame {count}")
capture.release()

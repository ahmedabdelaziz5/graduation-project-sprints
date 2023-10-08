import cv2
from pytesseract import pytesseract
import db

# Defining paths to tesseract.exe
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Defining paths to the image we would be using
image_path = "dataset/4.jpg"

# Pre-Processing Image
img = cv2.imread(image_path)
resized_img = cv2.resize(img, (712, 512), interpolation=cv2.INTER_AREA)
cropped_img = resized_img[resized_img.shape[0]*-7//24:resized_img.shape[0]*-1//10, resized_img.shape[1]*3//-5:]
gray_img = cv2.cvtColor(cropped_img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(gray_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 16)

# Convert image to text
obj = pytesseract.image_to_string(img, lang='ara_number', config='--psm 7')
text = obj.replace(' ', '')[:14]

# save in database
try: # if id exists, ignore it
    db.insert_id(text)
except:
    pass

db.getIDs()

# show image after Processing
cv2.imshow("Display window", img)
k = cv2.waitKey(0)


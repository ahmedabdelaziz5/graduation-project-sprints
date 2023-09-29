import cv2
from pytesseract import pytesseract

# Defining paths to tesseract.exe
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Defining paths to the image we would be using
image_path = "2.jpg"

# Pre-Processing Image
img = cv2.imread(image_path)
img = img[img.shape[0]//4:img.shape[0]*2//3, img.shape[1]*2//-3:]
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 85, 33)

# Convert image to text
obj = pytesseract.image_to_string(img, lang='ara')

# Extracting text and removing symbols
text = ''
for i in range(len(obj)):
    if obj[i] in '@#$%^&*_+=,.:|;©\'"':
        continue
    text += obj[i]
text = text[:-1]

# Displaying the extracted text
print(text)

# save file
with open('Information Output.txt', 'w', encoding="utf-8") as file:
    file.write(text)

# show image after Processing
cv2.imshow("Display window", img)
k = cv2.waitKey(0)
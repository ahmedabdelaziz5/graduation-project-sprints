import cv2
from pytesseract import pytesseract

# Defining paths to tesseract.exe
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Defining paths to the image we would be using
img_path = "khadija.jpg"


# function to extract id number from arabic national id card
def id_no(path):
    # Pre-Processing Image
    img = cv2.imread(path)
    resized_img = img[img.shape[0] * -1 // 3:img.shape[0] * -1 // 10, img.shape[1] * 3 // -5:]
    colored_img = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    threshold = cv2.adaptiveThreshold(colored_img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 75, 22)

    # Extracting id number
    text = pytesseract.image_to_string(threshold, lang='ara_number')
    text.replace(' ', '')
    # Displaying the extracted text and the original image
    cv2.imshow('img', resized_img)
    print(text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

id_no(img_path)
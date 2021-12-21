#testing tesseract for first time

import pytesseract as tess
#this second part: adding tesseract as an environment variable

tess.pytesseract.tesseract_cmd = r'S:\Tesseract_OCR\tesseract.exe'
#other modules within pytesseract and outside
from PIL import Image
import cv

img = Image.open('actual_receipt.jpg')


#processing
#not sure what the L does, must check
img = Image.open('actual_receipt.jpg').convert('L')
#ret,img = cv2.threshold(np.array(img), 125, 255, cv2.THRESH_BINARY)
#why not in cv, what is cv2? creates error

#img = Image.fromarray(img.astype(np.uint8))
# now image type saying it doesnt have an astype attribute?

text = tess.image_to_string(img)



print(text)




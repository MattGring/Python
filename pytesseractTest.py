# playing around with pytesseract

# imports:
from pytesseract import image_to_string
from PIL import Image

# this is how you work it
print(image_to_string(Image.open('C:\\Python34\\Lib\\site-packages\\pytesseract\\test.png')))

# or
stuff = image_to_string(Image.open('C:\\Python34\\Lib\\site-packages\\pytesseract\\test.png'))

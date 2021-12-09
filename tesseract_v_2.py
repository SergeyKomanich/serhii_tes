import pytesseract
from PIL import Image

img = Image.open("text_pa.jpg")
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

custom_config = r'--oem 3 --psm 13'
text = pytesseract.image_to_string(img, config=custom_config)
print(text.strip())

with open('chirurgia.txt', 'a') as f:
    f.write(text.strip()+"\n")
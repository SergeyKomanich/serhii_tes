import pytesseract
from PIL import Image

img = Image.open("text_pa.jpg")
pytesseract.pytesseract.tesseract_cmd = r"/usr/bin/tesseract"

text = pytesseract.image_to_string(img, lang="ukr")
print(text.strip())

with open('text_from_image.txt', 'a') as f:
    f.write(text.strip()+"\n")

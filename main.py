import pytesseract
import PIL.Image
import openpyxl

myconfig = r"--psm 3 --oem 3"
text = pytesseract.image_to_string(PIL.Image.open("Images/test.png"), config=myconfig)
print(text)
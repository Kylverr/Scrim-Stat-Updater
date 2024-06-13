import pytesseract
import PIL.Image
import openpyxl

BOXES = [
    [710, 314, 1000, 346],
    [1044, 311, 1128, 344],
    [1155, 310, 1214, 345],
    [1255, 314, 1311, 346],
    [1350, 310, 1410, 343],
    [1447, 309, 1511, 340]
]

def text_from_box(image_path, given_box, myconfig):
    img = PIL.Image.open(image_path)
    box = (given_box[0], given_box[1], given_box[2], given_box[3])
    region = img.crop(box)
    text = pytesseract.image_to_string(region, config=myconfig)
    return text

name_config = r"--psm 3 --oem 3"
number_config = "--psm 6 -c tessedit_char_whitelist=0123456789"
for b in BOXES:
    print(text_from_box("Images/test.png", b, number_config))
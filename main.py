import pytesseract
from PIL import Image, ImageEnhance
import openpyxl
import cv2
import numpy as np

BOXES = [
    # first player
    [708, 314, 1000, 346],
    [1044, 311, 1128, 344],
    [1155, 310, 1214, 345],
    [1255, 314, 1311, 346],
    [1350, 310, 1410, 343],
    [1447, 309, 1511, 340],
    # second player
    [708, 366, 1002, 400],
    [1043, 367, 1131, 396],
    [1156, 368, 1214, 394],
    [1255, 372, 1311, 395],
    [1351, 371, 1413, 396],
    [1446, 369, 1510, 396],
    # third player
    [708, 418, 1002, 442],
    [1043, 419, 1131, 450],
    [1156, 420, 1214, 448],
    [1255, 424, 1311, 449],
    [1355, 423, 1413, 450],
    [1450, 421, 1510, 450],
    # fourth player
    [708, 568, 1002, 591],
    [1043, 580, 1131, 600],
    [1156, 580, 1214, 600],
    [1255, 580, 1311, 600],
    [1355, 580, 1413, 600],
    [1450, 580, 1510, 600],
    # fifth player
    [708, 625, 1002, 655],
    [1043, 635, 1131, 660],
    [1156, 635, 1214, 660],
    [1255, 635, 1311, 660],
    [1355, 635, 1413, 660],
    [1450, 635, 1510, 660],
]

NAME_CONFIG = r"--psm 3 --oem 3"
NUMBER_CONFIG = "--psm 6 -c tessedit_char_whitelist=0123456789"

def text_from_box(image_path, given_box, myconfig):
    img = Image.open(image_path)
    box = (given_box[0], given_box[1], given_box[2], given_box[3])
    region = img.crop(box)
    region = preprocess_image(region)
    text = pytesseract.image_to_string(region, config=myconfig)

    # if a name couldn't be found, probably due to tag
    if not text and myconfig == NAME_CONFIG:
        box = (given_box[0], given_box[1] - 5, given_box[2], given_box[3] - 10)
        region = img.crop(box)
        region = preprocess_image(region)
        text = pytesseract.image_to_string(region, config=myconfig)

    # return 0 if image_to_string returned nothing
    if not text:
        return "0"
    return text

def preprocess_image(region):
    # Enhance the image contrast
    enhancer = ImageEnhance.Contrast(region)
    region = enhancer.enhance(2)
    
    # Convert PIL Image to OpenCV format
    img = np.array(region)
    
    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Resize the image to improve OCR accuracy
    # img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    
    # Apply binary thresholding
    _, img = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)

    # Invert the colors
    img = cv2.bitwise_not(img)
    
    # Apply slight Gaussian Blur to reduce noise
    img = cv2.GaussianBlur(img, (3, 3), 0)
    
    # Convert back to PIL Image
    img = Image.fromarray(img)

    # Save the preprocessed image for debugging
    img.save('preprocessed_image.png')
    
    return img

cur_config = ""
for b in BOXES:
    if (b[0] == 708):
        cur_config = NAME_CONFIG
    print(text_from_box("Images/test.png", b, cur_config))
    cur_config = NUMBER_CONFIG
print(text_from_box("Images/test.png", BOXES[24], cur_config))
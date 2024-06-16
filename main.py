import pytesseract
from PIL import Image, ImageEnhance
import openpyxl
import cv2
import numpy as np
import re
import sys

"""
This script reads an image of a Rocket League end-game scoreboard (uncropped) and 
extracts data containing the name, score, number of goals, number of assists, number 
of saves, and number of shots of each player.

Author: Kyle Stewart
Date: 2024-06-16

Usage:
    python main.py <image_path>
"""

BOXES = [
    # first player
    [708, 310, 1000, 346],
    [1044, 308, 1128, 344],
    [1158, 316, 1205, 342],
    [1255, 314, 1311, 346],
    [1350, 310, 1410, 343],
    [1447, 309, 1511, 340],
    # second player
    [708, 362, 1002, 400],
    [1043, 367, 1131, 396],
    [1156, 368, 1214, 394],
    [1255, 372, 1311, 395],
    [1352, 373, 1410, 394],
    [1446, 369, 1510, 396],
    # third player
    [708, 418, 1000, 454],
    [1043, 419, 1131, 450],
    [1156, 420, 1214, 448],
    [1255, 424, 1311, 449],
    [1355, 423, 1413, 450],
    [1450, 421, 1510, 450],
    # fourth player
    [708, 568, 1002, 604],
    [1043, 580, 1131, 600],
    [1156, 580, 1214, 600],
    [1255, 580, 1311, 600],
    [1355, 580, 1413, 600],
    [1450, 580, 1510, 600],
    # fifth player
    [708, 625, 1002, 660],
    [1043, 630, 1131, 655],
    [1156, 630, 1214, 655],
    [1255, 630, 1311, 655],
    [1355, 630, 1413, 655],
    [1450, 630, 1505, 655],
    # sixth player
    [708, 678, 1002, 716],
    [1043, 683, 1131, 712],
    [1156, 683, 1214, 712],
    [1255, 683, 1311, 712],
    [1355, 685, 1400, 710],
    [1450, 683, 1510, 712]
]

NAME_CONFIG = r'--psm 7 --oem 3 -l eng'
NUMBER_CONFIG = r'--psm 6 -c tessedit_char_whitelist=0123456789'

def text_from_box(image_path, given_box, myconfig=NUMBER_CONFIG):
    """
    Extracts text within the specific pixel box from the image with the 
    specified path.

    Args:
        image_path (str): path to the image file from which data will be extracted 
        from
        given_box (array): [left, upper, right, lower] pixel array to search within
        myconfig: pytesseract config to help read data
    """

    # set correct config
    if (given_box[0] == 708):
        myconfig = NAME_CONFIG

    img = Image.open(image_path)
    box = (given_box[0], given_box[1], given_box[2], given_box[3])
    region = img.crop(box)
    region = preprocess_image(region)
    text = pytesseract.image_to_string(region, config=myconfig)

    # if a name couldn't be found, probably due to tag
    if not text and myconfig == NAME_CONFIG:
        box = (given_box[0], given_box[1] - 5, given_box[2], given_box[3] + 20)
        region = img.crop(box)
        region = preprocess_image(region)
        text = pytesseract.image_to_string(region, config=myconfig)

    # return 0 if image_to_string returned nothing
    if not text:
        return "0"
    removed_brackets_text = re.sub(r"\[.*?\]", "", text)
    cleaned_text = removed_brackets_text.strip()
    return cleaned_text

def preprocess_image(region):
    """
    Helper function that takes a region of an image and enhances it for 
    better reading/extraction.

    Args:
        region (array): region of image to enhance
    """
    # Enhance the image contrast
    enhancer = ImageEnhance.Contrast(region)
    region = enhancer.enhance(2)
    
    # Convert PIL Image to OpenCV format
    img = np.array(region)
    
    # Convert to grayscale
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Resize the image to improve OCR accuracy
    img = cv2.resize(img, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
    
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

def extract_game_info(filepath):
    """
        Extracts game info from the image with the specified path. Data is returned 
        in an array.

        Args:
            filepath (str): file path to image
    """
    game_info = []

    for b in BOXES:
        game_info.append(text_from_box(filepath, b))
    
    return game_info

if len(sys.argv) < 1:
    print("Invalid number of args given. Make sure you are only providing the path to the image you want scanned.")
    sys.exit(1)

extract_game_info(sys.argv[1])
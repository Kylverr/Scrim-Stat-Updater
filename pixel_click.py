import cv2

# Define a callback function to get the pixel coordinates
def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # Print the coordinates of the point clicked
        print(f'Pixel coordinates: ({x}, {y})')
        # Display the coordinates on the image window
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, f'({x}, {y})', (x, y), font, 0.5, (125, 125, 0), 2)
        cv2.imshow('image', img)

# Load an image
image_path = 'Images/test.png'
img = cv2.imread(image_path)

# Display the image in a window
cv2.imshow('image', img)

# Set the mouse callback function to capture click events
cv2.setMouseCallback('image', click_event)

# Wait for a key press and close the image window
cv2.waitKey(0)
cv2.destroyAllWindows()
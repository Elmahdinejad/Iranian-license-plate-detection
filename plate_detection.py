import cv2  
import numpy as np  
import easyocr  
import matplotlib.pyplot as plt  

# Load the Haar cascade for license plate detection  
plate_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')  

# Read the image  
carplate_img = cv2.imread("/content/drive/MyDrive/CarImage2.jpg")  # Adjust the path  

# Resize the image  
carplate_img = cv2.resize(carplate_img, (800, 600))  

# Convert the image to grayscale  
gray_img = cv2.cvtColor(carplate_img, cv2.COLOR_BGR2GRAY)  

# Apply Gaussian blur for noise reduction  
blurred_img = cv2.GaussianBlur(gray_img, (5, 5), 0)  

# Detect license plates  
plates = plate_cascade.detectMultiScale(blurred_img, scaleFactor=1.1, minNeighbors=5)  

if len(plates) > 0:  
    for (x, y, w, h) in plates:  
        # Extract the license plate region  
        plate_img = carplate_img[y:y + h, x:x + w]  

        # Show the extracted license plate image  
        plt.imshow(cv2.cvtColor(plate_img, cv2.COLOR_BGR2RGB))  
        plt.axis('off')  
        plt.title('Extracted License Plate Image')  
        plt.show()  

        # Step 1: Perform OCR on the original image  
        reader = easyocr.Reader(['fa', 'en', 'ar'])  # Add Arabic language support  
        detected_texts_original = reader.readtext(carplate_img)  

        # Print detected texts from the original image  
        print("Detected Text from Original Image:")  
        for text in detected_texts_original:  
            print("Detected Text:", text[1])  # text[1] contains the recognized string  

        # Step 2: Perform OCR on the extracted plate image  
        detected_texts_plate = reader.readtext(plate_img)  

        # Print detected texts from the extracted plate image  
        print("Detected Text from Extracted License Plate Image:")  
        for text in detected_texts_plate:  
            print("Detected Text:", text[1])  # text[1] contains the recognized string  

else:  
    print("No license plates detected.")
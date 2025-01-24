# License Plate Detection and OCR with EasyOCR

## Overview

This project implements a simple pipeline for detecting license plates in images using OpenCV and performing Optical Character Recognition (OCR) with EasyOCR. The code loads a pre-trained Haar cascade classifier to detect Russian license plates and utilizes EasyOCR to read the text from the detected areas.

## Code Explanation

## Key Components

** Libraries Used:**

cv2: OpenCV for image processing.
numpy: For numerical operations.
easyocr: For performing OCR on license plates.
matplotlib.pyplot: For displaying images.
Haar Cascade for License Plate Detection:

The project employs a Haar cascade classifier specifically for recognizing Russian license plates. This is loaded using OpenCV's cv2.CascadeClassifier.
Image Loading:

An image containing a car is loaded from a specified path using OpenCV’s cv2.imread method.

The code initializes the required libraries and sets up the necessary components for image detection.

## Current Status

This implementation is in progress. Additional features such as improved image preprocessing, handling multiple detections, and enhancing OCR accuracy are planned for future updates. The current model serves as a foundation for further development in license plate detection and recognition systems.

## Future Work

Refining the OCR process for better accuracy.
Handling various license plate formats and languages.
Comprehensive testing with various images.
Enhancing the user interface for easier interaction.


**Please note that this project is not completed and will be updated in the future as development continues.**
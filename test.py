import cv2
import numpy as np

def find_rice_color(image):
    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define the lower and upper bounds for different colors of rice grains
    lower_red = np.array([0, 50, 50])        # Lower bound for red color
    upper_red = np.array([10, 255, 255])      # Upper bound for red color

    lower_white = np.array([0, 0, 180])       # Adjusted lower bound for white color
    upper_white = np.array([255, 30, 255])    # Adjusted upper bound for white color

    lower_black = np.array([0, 0, 0])         # Adjusted lower bound for black color
    upper_black = np.array([180, 255, 30])    # Adjusted upper bound for black color

    # Create binary masks using inRange function for each color
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)
    mask_black = cv2.inRange(hsv_image, lower_black, upper_black)

    # Combine the masks to get the final result
    mask_combined = cv2.bitwise_or(mask_red, mask_white)
    mask_combined = cv2.bitwise_or(mask_combined, mask_black)

    # Apply the combined mask to the original image
    result = cv2.bitwise_and(image, image, mask=mask_combined)

    # Print the detected color in the terminal
    #print(mask_red)
    #print(mask_black)
   # print(mask_white)
    print(np.sum(mask_red))
    print(np.sum(mask_black))
    print(np.sum(mask_white))
    if np.sum(mask_red) > np.sum(mask_white) and np.sum(mask_red) > np.sum(mask_black):
        print("Detected color: Red")
    elif np.sum(mask_white) > np.sum(mask_red) and np.sum(mask_white) >  np.sum(mask_black) :
        print("Detected color: White")
    else :
        print("Detected color: Black")
    # else:
    #     print("No specific color detected")

    return result

# Example usage
image = cv2.imread("BlackRice1.jpg")  # Replace with the path to your image
result_image = find_rice_color(image)

# Save the original and result images to disk
cv2.imwrite("original_image.jpg", image)
cv2.imwrite("result_image.jpg", result_image)

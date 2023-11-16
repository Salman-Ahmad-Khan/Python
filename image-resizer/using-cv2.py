import cv2
print(cv2.__version__)

"""
image resizer program, using the OpenCV library (cv2)
"""



def resize_image_cv2(input_path, output_path, new_size):
    try:
        # Read the image
        img = cv2.imread(input_path)

        # Resize the image
        resized_img = cv2.resize(img, new_size)

        # Save the resized image
        cv2.imwrite(output_path, resized_img)

        print("Image resized successfully.")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
input_image_path = "image1.jpeg"  # Replace with the path to your input image
output_image_path = "output.jpg"  # Replace with the desired output path
new_size = (600, 200)  # Replace with the desired width and height

resize_image_cv2(input_image_path, output_image_path, new_size)

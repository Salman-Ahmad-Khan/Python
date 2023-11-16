from PIL import Image

"""
 image resizer program, using the Python Imaging Library (PIL), now known as Pillow. 
"""

def resize_image(input_path, output_path, new_size):
    try:
        # Open the image file
        with Image.open(input_path) as img:
            # Resize the image
            resized_img = img.resize(new_size)
            # Save the resized image
            resized_img.save(output_path)
        print("Image resized successfully.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
input_image_path = "image1.jpeg"  # Replace with the path to your input image
output_image_path = "output1.jpg"  # Replace with the desired output path
new_size = (300, 200)  # Replace with the desired width and height

resize_image(input_image_path, output_image_path, new_size)

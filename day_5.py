# Puzzle: Wallpaper Image Scaler

# Write a program that resizes an image to fit an Android phone's wallpaper dimensions while maintaining its aspect ratio.

# Pseudocode:

#     Input the dimensions of the phone's wallpaper (width and height).
#     Input the dimensions of the original image (width and height).
#     Calculate the scaling factor to maintain the aspect ratio:
#         Use the smaller scaling factor of width and height.
#     Compute the new width and height for the image using the scaling factor.
#     Ensure the image is centered in the wallpaper dimensions (add padding if needed).
#     Output the new dimensions and any adjustments for centering.


from PIL import Image

def resize_image_simple(image_path, target_width, target_height):
    # Open the image
    with Image.open(image_path) as img:
        # Resize while maintaining aspect ratio
        img.thumbnail((target_width, target_height))  # Automatically maintains aspect ratio
        
        # Save the resized image
        img.save("resized_wallpaper_simple.jpg")
        print(f"Image resized and saved as 'resized_wallpaper_simple.jpg'. New size: {img.size}")

# Example Usage:
resize_image_simple("your_image.jpg", 1440, 3120)  # Replace "your_image.jpg" with your file path


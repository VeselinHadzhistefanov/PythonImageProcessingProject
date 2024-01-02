import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from image_detection import detect_image
from image_list import list_image_files

# Get image files
print("These are the image files:")
folder_path = 'images'
image_files = list_image_files(folder_path)

# Print image files
for n, file in enumerate(image_files):
    print(n, file)

# Input image number
img_number_input = input("\nPlease enter an number for an image: ")

# Convert the input to int
try:
    img_num = int(img_number_input)
    print(f"You are using the image: {img_num}")
except ValueError:
    print("That's not a valid image number. Please try again.")

# Read the image
img_filepath = image_files[img_num]
img = mpimg.imread(img_filepath)

detected_image = detect_image(img_filepath)
detected_image_rgb = cv2.cvtColor(detected_image, cv2.COLOR_BGR2RGB)

# Display the detected image
plt.imshow(detected_image_rgb)
plt.axis('off')  # To turn off the axis
plt.title(img_filepath)  # To add a title
plt.show()

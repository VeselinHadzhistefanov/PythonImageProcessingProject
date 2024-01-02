import os
def list_image_files(folder_path):
    # Supported image file extensions
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp']

    # List to store the names of image files
    image_files = []

    # Walking through the folder and its subfolders
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Check if the file extension is in the list of image extensions
            if any(file.lower().endswith(ext) for ext in image_extensions):
                # Add the file to the list
                image_files.append(os.path.join(root, file))

    return image_files

# List image files
folder_path = 'images'
image_files = list_image_files(folder_path)
for n, file in enumerate(image_files):
    print(n, file)

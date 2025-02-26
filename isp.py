import os
import cv2

# Configuration parameters
photos_folder = r'C:\dataset'  # Path to the folder containing photos
blurred_folder_name = 'blurred'  # Name of the folder for blurred images
sharpness_threshold = 20  # Sharpness threshold value
recursive_search = False  # Enable or disable recursive search

# Function to calculate image sharpness using the Friedman criterion
def calculate_sharpness(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    laplacian_var = cv2.Laplacian(gray, cv2.CV_64F).var()
    return laplacian_var

# Create the folder for blurred images if it does not exist
blurred_folder = os.path.join(photos_folder, blurred_folder_name)
if not os.path.exists(blurred_folder):
    os.makedirs(blurred_folder)

def process_images(folder_path):
    # Iterate over all files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if os.path.isdir(file_path) and recursive_search:
            process_images(file_path)  # Recursive call for subdirectories

        elif filename.endswith('.jpg') or filename.endswith('.png'):
            photo_path = file_path

            # Load the image
            image = cv2.imread(photo_path)

            if image is None:
                continue

            # Calculate the sharpness of the image
            sharpness_score = calculate_sharpness(image)

            # Check if the image is blurry
            if sharpness_score < sharpness_threshold:
                print(f"Moving blurred image: {filename} to folder '{blurred_folder_name}'")
                blurred_photo_path = os.path.join(blurred_folder, filename)
                os.rename(photo_path, blurred_photo_path)  # Move the file
            else:
                print(f"Image is clear: {filename}")

# Start processing images in the specified folder
process_images(photos_folder)
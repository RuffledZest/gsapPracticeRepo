import os

# Specify the folder path where the images are stored
folder_path = 'ballAnimation\BlenderBallAnimation'

# Loop through all files in the folder
for filename in os.listdir(folder_path):
    # Check if the file is a jpg image
    if filename.endswith('.jpg'):
        # Extract the name without extension and remove leading zeros
        new_name = str(int(filename.split('.')[0])) + '.jpg'

        # Get the full paths for renaming
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)

        # Rename the file
        os.rename(old_file, new_file)
        print(f'Renamed: {filename} -> {new_name}')

print("Renaming completed!")
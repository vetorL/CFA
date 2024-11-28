import os
from io import BytesIO
from PIL import Image
import re

# Fixed size for resizing
x, y = 128, 64  # Adjust dimensions as needed

# Directory containing subdirectories with images
assets_dir = "assets"

# Output Python file
output_file = "images_repo.py"

# Initialize output file
with open(output_file, "w") as f:
    f.write("# Image byte arrays with inverted colors\n\n")


# Sorting key for natural ordering
def natural_sort_key(s):
    return [
        int(text) if text.isdigit() else text.lower() for text in re.split("(\d+)", s)
    ]


# Process each subdirectory in the assets directory
for subdir in sorted(os.listdir(assets_dir), key=natural_sort_key):
    subdir_path = os.path.join(assets_dir, subdir)

    # Skip non-directory files
    if not os.path.isdir(subdir_path):
        continue

    # Initialize list for the current directory
    img_list = []
    img_counter = 1

    # Process images in the current directory
    for filename in sorted(os.listdir(subdir_path), key=natural_sort_key):
        file_path = os.path.join(subdir_path, filename)

        # Check if the file is an image
        try:
            im = Image.open(file_path).convert("1")
        except Exception as e:
            print(f"Skipping non-image file: {filename} in {subdir}")
            continue

        # Resize image
        im_resize = im.resize((x, y))

        # Invert colors
        inverted_im = Image.eval(im_resize, lambda px: 255 - px)

        buf = BytesIO()
        inverted_im.save(buf, "ppm")
        byte_im = buf.getvalue()

        # Calculate offset
        temp = len(str(x) + " " + str(y)) + 4

        # Extract byte array and save to Python file
        image_bytes = byte_im[temp:]
        var_name = f"{subdir}_img_{img_counter}"
        img_list.append(var_name)  # Add variable name to list
        with open(output_file, "a") as f:
            f.write(f"{var_name} = bytearray({repr(image_bytes)})\n\n")
        img_counter += 1

    # Write the list of images for the current directory
    with open(output_file, "a") as f:
        f.write(f"{subdir}_images_list = [{', '.join(img_list)}]\n\n")

print(f"Processed images with inverted colors saved to {output_file}.")

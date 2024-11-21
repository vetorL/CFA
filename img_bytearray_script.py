import os
from io import BytesIO
from PIL import Image

# Fixed size for resizing
x, y = 128, 64  # Adjust dimensions as needed

# Directory containing images
assets_dir = "assets"

# Output Python file
output_file = "images_repo.py"

# Initialize output file
with open(output_file, "w") as f:
    f.write("# Image byte arrays\n\n")

# Initialize image list
img_list = []

# Process each image in the assets directory
img_counter = 1
for filename in os.listdir(assets_dir):
    file_path = os.path.join(assets_dir, filename)

    # Check if the file is an image
    try:
        im = Image.open(file_path).convert("1")
    except Exception as e:
        print(f"Skipping non-image file: {filename}")
        continue

    # Resize image
    im_resize = im.resize((x, y))
    buf = BytesIO()
    im_resize.save(buf, "ppm")
    byte_im = buf.getvalue()

    # Calculate offset
    temp = len(str(x) + " " + str(y)) + 4

    # Extract byte array and save to Python file
    image_bytes = byte_im[temp:]
    var_name = f"img_{img_counter}"
    img_list.append(var_name)  # Add variable name to list
    with open(output_file, "a") as f:
        f.write(f"{var_name} = bytearray({repr(image_bytes)})\n\n")
    img_counter += 1

# Write the list of images to the Python file
with open(output_file, "a") as f:
    f.write(f"img_list = [{', '.join(img_list)}]\n")

print(f"Processed images saved to {output_file}.")

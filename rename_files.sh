#!/bin/bash

# Directory containing the files (change to your target directory)
DIRECTORY="./"

# Iterate over all files matching the pattern
for file in "$DIRECTORY"pixil-frame-*.png; do
  # Extract the number from the filename using parameter expansion
  number=$(basename "$file" | sed -E 's/pixil-frame-([0-9]+)\.png/\1/')
  
  # Construct the new filename
  new_filename="$DIRECTORY$number.png"
  
  # Rename the file
  mv "$file" "$new_filename"
  
  echo "Renamed: $file -> $new_filename"
done

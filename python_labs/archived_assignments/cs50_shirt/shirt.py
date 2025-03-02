# https://cs50.harvard.edu/python/2022/psets/6/shirt/

from PIL import Image, ImageOps
import sys
import os

def main():
    # Check for the correct number of arguments
    # Should be 3 - first is file with shirt alpha layer
    # second is the desired output filename
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    # Make sure the filenames end in .jpg .jpeg or .png
    valid_extensions = [".jpg", ".jpeg", ".png"]

    for file_name in sys.argv[1:3]:
        if os.path.splitext(file_name)[1].lower() not in valid_extensions:
            sys.exit("Not a valid image format - must be .jpg, .jpeg, or .png")

    # Try opening the input files:
    try:
        # Open the input file and the shirt file with transparency
        with Image.open(sys.argv[1]) as subject, Image.open("shirt.png") as original_shirt:
            # Extract the horizontal and vertical height (in pixels) from the target photo
            # i.e. the one who will "wear the shirt"
            h,v = subject.width, subject.height
            # Create a resized object from the shirt, using the fit function to crop/resize based
            # on the extract picture resolution from the previous line
            resized_shirt = ImageOps.fit(original_shirt, (h,v))
            # resized_shirt.save("testing_shirt.png") <- used to confirm the resized_shirt image
            subject.paste(resized_shirt, resized_shirt)
            subject.save(sys.argv[2])        
    except FileNotFoundError:
        sys.exit("Input file does not exist")



if __name__ == "__main__":
    main()
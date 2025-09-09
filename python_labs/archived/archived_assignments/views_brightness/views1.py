import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

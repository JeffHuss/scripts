import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()

        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            writer.writerow(
                {
                    "id": row["id"],
                    "english_title": row["english_title"],
                    "japanese_title": row["japanese_title"],
                    "brightness": round(brightness, 2),
                }
            )


def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()

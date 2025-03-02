import numpy as np
from PIL import Image
import csv

def main():
    with open("views.csv") as views, open("analysis.csv", "w") as analysis:
        reader = csv.DictReader(views)
        writer = csv.DictWriter(analysis, fieldnames=reader.fieldnames + ["brightness"])
        writer.writeheader()
        for row in reader:
            brightness = calculate_brightness(f"{row['id']}.jpeg")
            row["brightness"] = round(brightness, 2)
            writer.writerow(row)
            # writer.writerow(
            #     {
            #         "id": row["id"],
            #         "english_title": row["english_title"],
            #         "japanese_title": row["japanese_title"],
            #         "brightness": brightness
            #     }
            # )
            
            
            

def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness

if __name__ == "__main__":
    main()
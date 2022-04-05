import glob
from PIL import Image

UPPER_LEFT = [1499, 9]
LOWER_RIGHT = [1655, 96]
HALFEN_FRAMES = True

files = glob.glob("./img_data/*.png")
files.sort()

count = 0
skip = False

for file_number, file in enumerate(files):
    if count % 20 == 0:
        print(f"{file_number}/{len(files)} completed")

    if HALFEN_FRAMES and skip:
        skip = False
        continue

    img = Image.open(file)

    # Check if upper left bound is a transparent pixel
    # If it is transparent, the entire area has not been created yet and the file should be skipped
    if (0, 0, 0, 0) == img.getpixel((UPPER_LEFT[0], UPPER_LEFT[1])):
        continue

    img = img.crop((UPPER_LEFT[0], UPPER_LEFT[1], LOWER_RIGHT[0], LOWER_RIGHT[1]))

    file_name = f"./out/{count}.png"
    img.save(file_name)

    count += 1
    skip = True

import glob
from PIL import Image

UPPER_LEFT = [269, 887]
LOWER_RIGHT = [719, 1140]

files = glob.glob("./img_data/*.png")
files.sort()

count = 0

for file in files:
    img = Image.open(file).crop((UPPER_LEFT[0], UPPER_LEFT[1], LOWER_RIGHT[0], LOWER_RIGHT[1]))
    file_name = f"./out/{count}.png"
    img.save(file_name)

    if count % 20 == 0:
        print(f"{count}/{len(files)} completed")

    count += 1

# r/place timelapse creator

This simple script allows the creation of timelapses of r/place with custom bounds.

## How to use

1. run `pip install -r requirement.txt`
2. open `main.py` and change `UPPER_LEFT` and `LOWER_RIGHT` coordinates to define custom bounds
3. download image data from https://zevs.me/rplace_archive.7z. Extract the archive and place all the images in a folder called `img_data`
4. create a folder called `out`
5. run main.py
6. install ffmpeg and run `ffmpeg -i %d.png -r 60 -c:v libx264 -crf 24 -vf scale=w=1920:h=1080 -sws_flags neighbor output.mkv` to create the video (if you are doing a very small area, it might be more space efficient and visually look the same to create a 1280x720 video instead of a 1920x1080 video. If you are doing a particularly large area, and you notice imperfections in the video, try turning down -crf 24 to a lower number to improve the output quality. Feel free to mess with this command to get the perfect balance of filesize and quality if you'd like.)

## notes

The variable HALFEN_FRAMES controls if every other frame should be skipped. I keep this enabled to cut down on video length and execution time.

If you have any questions about usage, email me at mail@themimegas.com, open a github issue, or contact me on discord at Cat Meow Meow#7380. I'd also be happy to run the script for you and just send you the result.
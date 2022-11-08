from PIL import Image
import os
from math import *

img_folder = "img"

nb_imgs = len(os.listdir(img_folder))

atlas_len = ceil(sqrt(nb_imgs))

img_len = Image.open(os.path.join(img_folder, os.listdir(img_folder)[0])).width

atlas = Image.new(
    "RGB", (atlas_len * img_len, atlas_len * img_len))

idx = 0

for filename in os.listdir(img_folder):
    file = os.path.join(img_folder, filename)
    if os.path.isfile(file):
        img = Image.open(file)
        x = (idx % atlas_len) * img_len
        y = (idx // atlas_len) * img_len
        idx += 1
        atlas.paste(img, (atlas_len * img_len-x-img_len, y, atlas_len *
                    img_len-x, y+img_len))

atlas.save(os.path.join(img_folder, "atlas.png"))



def save_with_unique_name(file):
    return


def generate_flipbook(working_directory, images_folder, output_name="flipbook"):
    import os
    import math
    from PIL import Image
    from img_utils import unique_file_name

    input_dir = os.path.join(working_directory, images_folder)
    nb_imgs = len(os.listdir(input_dir))

    atlas_len = math.ceil(math.sqrt(nb_imgs))

    img_len = Image.open(os.path.join(
        input_dir, os.listdir(input_dir)[0])).width

    atlas = Image.new(
        "RGB", (atlas_len * img_len, atlas_len * img_len))

    idx = 0

    for filename in os.listdir(input_dir):
        file = os.path.join(input_dir, filename)
        if os.path.isfile(file):
            img = Image.open(file)
            x = (idx % atlas_len) * img_len
            y = (idx // atlas_len) * img_len
            idx += 1
            atlas.paste(img, (atlas_len * img_len-x-img_len, y, atlas_len *
                        img_len-x, y+img_len))

    atlas.save(unique_file_name(os.path.join(
        working_directory, f"{output_name}.png")))



def save_with_unique_name(file):
    return


def generate_flipbook(working_directory, images_folder, output_name="flipbook", overwrite_previous_flipbook=False):
    import os
    import math
    from PIL import Image
    from . import unique_file_name
    from . import ImageBatch

    batch = ImageBatch(os.path.join(working_directory, images_folder))

    nb_imgs = len(batch.images)
    atlas_len = math.ceil(math.sqrt(nb_imgs))
    img_len = batch.common_size[0]

    atlas = Image.new(
        "RGBA", (atlas_len * img_len, atlas_len * img_len))

    idx = 0

    for img in batch.images:
        x = (idx % atlas_len) * img_len
        y = (idx // atlas_len) * img_len
        idx += 1
        atlas.paste(img, (atlas_len * img_len-x-img_len, y, atlas_len *
                    img_len-x, y+img_len))

    flipbook_path = os.path.join(working_directory, f"{output_name}.png")
    if not overwrite_previous_flipbook:
        flipbook_path = unique_file_name(flipbook_path)

    atlas.save(flipbook_path)

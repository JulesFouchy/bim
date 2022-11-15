import enum
from numbers import Real


def save_with_unique_name(file):
    return


class LRDirection(enum.Enum):
    LEFT_TO_RIGHT = enum.auto()
    RIGHT_TO_lEFT = enum.auto()


class TBDirection(enum.Enum):
    TOP_TO_BOTTOM = enum.auto()
    BOTTOM_TO_TOP = enum.auto()


def flip_if(condition: bool, value: Real, max: Real):
    if not condition:
        return value

    return max - 1 - value


def generate_flipbook(
        working_directory,
        images_folder,
        output_name="flipbook",
        overwrite_previous_flipbook=False,
        lr_dir=LRDirection.LEFT_TO_RIGHT,
        tb_dir=TBDirection.TOP_TO_BOTTOM,
):
    import os
    import math
    from PIL import Image
    from . import unique_file_name
    from . import ImageBatch

    Image.MAX_IMAGE_PIXELS = 933120000

    batch = ImageBatch(os.path.join(working_directory, images_folder))

    nb_imgs = len(batch)
    atlas_len = math.ceil(math.sqrt(nb_imgs))
    img_len = batch.common_size[0]

    atlas = Image.new(
        "RGBA", (atlas_len * img_len, atlas_len * img_len))

    idx = 0

    for img in batch:
        x = idx % atlas_len
        y = idx // atlas_len
        x = flip_if(lr_dir == LRDirection.RIGHT_TO_lEFT, x, atlas_len)
        y = flip_if(tb_dir == TBDirection.BOTTOM_TO_TOP, y, atlas_len)
        idx += 1
        atlas.paste(img, (
            x*img_len, y*img_len,
            (x+1)*img_len, (y+1)*img_len)
        )

    flipbook_path = os.path.join(working_directory, f"{output_name}.png")
    if not overwrite_previous_flipbook:
        flipbook_path = unique_file_name(flipbook_path)

    atlas.save(flipbook_path)

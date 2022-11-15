

def size_that_fits(size, aspect_ratio):
    from . import aspect_ratio as calc_aspect_ratio
    current_aspect_ratio = calc_aspect_ratio(size)

    if aspect_ratio > current_aspect_ratio:
        return (size[0], size[1] / aspect_ratio)
    else:
        return (size[0] * aspect_ratio, size[1])


def crop(
    working_directory,
    images_folder,
    output_folder,
    aspect_ratio: float,
):
    import os
    from . import ImageBatch
    from PIL import Image

    batch = ImageBatch(os.path.join(working_directory, images_folder))
    size = size_that_fits(batch.common_size, aspect_ratio)

    for img in batch:
        cropped = img.crop((
            batch.common_size[0] / 2 - size[0] / 2,
            batch.common_size[1] / 2 - size[1] / 2,
            batch.common_size[0] / 2 + size[0] / 2,
            batch.common_size[1] / 2 + size[1] / 2,
        ))
        cropped.save(os.path.join(working_directory, output_folder, img.name))

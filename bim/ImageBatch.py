from collections.abc import Iterator
from PIL import Image
from typing import List


class MismatchedImageSizes(Exception):
    def __init__(self, name_of_faulty_image, faulty_size, common_size):
        self.message = f'Image "{name_of_faulty_image}" has size {faulty_size}, while other images have size {common_size}.'
        super().__init__(self.message)


class MismatchedImageExtensions(Exception):
    def __init__(self, name_of_faulty_image, faulty_extension, common_extension):
        self.message = f'Image "{name_of_faulty_image}" has extension {faulty_extension}, while other images have extension {common_extension}.'
        super().__init__(self.message)


class ImageFolderIterator:
    def __init__(self, images_dir):
        import os
        self.dir_iterator = iter(os.listdir(images_dir))
        self.images_dir = images_dir

    def __next__(self):
        from PIL import Image
        import os

        file = next(self.dir_iterator)
        img = Image.open(os.path.join(self.images_dir, file))
        img.name = file
        return img


class ImageBatch:
    def __init__(self, images_dir):
        import os
        from pathlib import Path
        import PIL

        self.common_size = None
        self.common_extension = None
        self.images_dir = images_dir

        for filename in os.listdir(images_dir):
            file = os.path.join(images_dir, filename)
            if not os.path.isfile(file):
                continue
            try:
                # Open image
                img = Image.open(file)

                # Check common size
                if self.common_size and img.size != self.common_size:
                    raise MismatchedImageSizes(
                        Path(file).name, img.size, self.common_size)
                self.common_size = img.size

                # Check common extension
                ext = img.format
                if self.common_extension and ext != self.common_extension:
                    raise MismatchedImageExtensions(
                        Path(file).name, ext, self.common_extension)
                self.common_extension = ext

            except(PIL.UnidentifiedImageError):  # This was not an image file, no problem
                continue

    def __iter__(self) -> Iterator[Image.Image]:
        return ImageFolderIterator(self.images_dir)

    def __len__(self) -> int:
        import os
        return len(os.listdir(self.images_dir))

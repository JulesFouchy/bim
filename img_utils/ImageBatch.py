

class MismatchedImageSizes(Exception):
    def __init__(self, name_of_faulty_image, faulty_size, common_size):
        self.message = f'Image "{name_of_faulty_image}" has size {faulty_size}, while other images have size {common_size}.'
        super().__init__(self.message)


class MismatchedImageExtensions(Exception):
    def __init__(self, name_of_faulty_image, faulty_extension, common_extension):
        self.message = f'Image "{name_of_faulty_image}" has extension {faulty_extension}, while other images have extension {common_extension}.'
        super().__init__(self.message)


class ImageBatch:
    def __init__(self, images_dir):
        import PIL
        from PIL import Image
        import os
        from pathlib import Path

        self.images = []
        self.common_size = None
        self.common_extension = None

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

                # Add image
                self.images.append(img)

            except(PIL.UnidentifiedImageError):  # This was not an image file, no problem
                continue

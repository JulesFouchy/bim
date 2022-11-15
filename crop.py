import bim

bim.crop(
    working_directory=bim.current_folder(__file__),
    images_folder="img",
    output_folder="img_out",
    aspect_ratio=1
)

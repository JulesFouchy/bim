import bim

bim.generate_flipbook(
    working_directory=bim.current_folder(__file__),
    images_folder="img",
    overwrite_previous_flipbook=True,
)

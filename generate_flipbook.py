import bim

bim.generate_flipbook(
    working_directory=bim.current_folder(__file__),
    images_folder="img",
    output_name="flipbook",
    overwrite_previous_flipbook=True,
    lr_dir=bim.LRDirection.LEFT_TO_RIGHT,
    tb_dir=bim.TBDirection.TOP_TO_BOTTOM,
)

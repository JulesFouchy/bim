

def unique_file_name(path):
    import os
    from pathlib import Path

    ret_path = path
    id = 1
    while os.path.exists(ret_path):
        p = Path(path)
        ret_path = p.with_stem(f"{p.stem} ({id})")
        id += 1

    return ret_path

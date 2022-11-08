

def current_folder(file):
    from pathlib import Path
    return Path(file).parent

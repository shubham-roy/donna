from os import mkdir
from os.path import isdir


def make_directory(path: str) -> None:
    """
    Creates a directory at the specified path, if not already present.
    """
    if isdir(path):
        return
    mkdir(path)

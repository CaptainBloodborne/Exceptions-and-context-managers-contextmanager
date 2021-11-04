import os.path
from contextlib import contextmanager
from os import getcwd, chdir


@contextmanager
def cd_context(path: str):
    current_dir = getcwd()
    try:
        chdir(path)
        if os.path.isdir(path) or os.path.exists(path):
            raise ValueError

    finally:
        chdir(current_dir)

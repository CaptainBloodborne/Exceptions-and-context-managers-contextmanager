import os.path
from contextlib import contextmanager
from os import getcwd, chdir


@contextmanager
def cd_context(path: str):
    current_dir = getcwd()
    try:
        if not os.path.isdir(path) or not os.path.exists(path):
            raise ValueError
        chdir(path)

    finally:
        chdir(current_dir)

import os.path
from contextlib import contextmanager
from os import chdir, getcwd


@contextmanager
def cd_context(path: str):
    current_dir = getcwd()

    if not os.path.isdir(path) or not os.path.exists(path):
        raise ValueError
    chdir(path)
    yield f"Directory changed to {path}"
    chdir(current_dir)

import os.path
from contextlib import contextmanager
import os


@contextmanager
def cd_context(path: str):
    current_dir = os.getcwd()

    if not os.path.isdir(path) or not os.path.exists(path):
        raise ValueError
    os.chdir(path)
    yield f"Directory changed to {path}"
    os.chdir(current_dir)

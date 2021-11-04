from contextlib import contextmanager
from os import getcwd, chdir


@contextmanager
def cd_context(path: str):
    current_dir = getcwd()
    try:
        chdir(path)
    except FileNotFoundError:
        raise ValueError
    finally:
        chdir(current_dir)

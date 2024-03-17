from re import compile
from os.path import isfile

def validate_url(url) -> bool:
    regexp = compile(r"https?://vadapav.mov/[a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}/?")
    if regexp.match(url):
        return True
    return False

def validate_path(path) -> bool:
    return isfile(path)
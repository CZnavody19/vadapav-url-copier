from requests import get
from rich.prompt import Prompt

def get_html(url) -> str:
    return get(url).text

def append_to_file(path, data):
    with open(path, "a") as f:
        f.write(data + "\n")

def clear_file(path):
    with open(path, "w") as f:
        f.write("")

def join_url(url):
    return "https://vadapav.mov{}".format(url)

def get_input(prompt) -> str:
    return Prompt.ask(prompt)
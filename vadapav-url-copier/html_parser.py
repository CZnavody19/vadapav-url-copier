from bs4 import BeautifulSoup

def parse_title(html):
    parsed = BeautifulSoup(html, features="html.parser")
    extracted = parsed.body.find("div", attrs={'class':'directory'}).find("div")
    return extracted.text.replace("\n", "").strip()

def parse_seasons(html):
    parsed = BeautifulSoup(html, features="html.parser")
    extracted = parsed.body.find("div", attrs={'class':'directory'}).find("ul").find_all("li")
    seasons = []
    for i in extracted:
        li_div = i.find("div", attrs={'class':'centerflex name-div'})
        if li_div:
            li_a = li_div.find("a")
            if li_a.text.startswith("Season"):
                seasons.append((li_a.text, li_a.attrs['href']))
    return seasons

def parse_episodes(html):
    parsed = BeautifulSoup(html, features="html.parser")
    extracted = parsed.body.find("div", attrs={'class':'directory'}).find("ul").find_all("li")
    episodes = []
    for i in extracted:
        li_div = i.find("div", attrs={'class':'centerflex name-div'})
        if li_div:
            li_a = li_div.find("a")
            if not "parent directory" in li_a.text.lower():
                episodes.append((li_a.text, li_a.attrs['href']))
    return episodes
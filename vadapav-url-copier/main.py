from rich import print
from argparse import ArgumentParser
from utils import get_html, append_to_file, join_url, clear_file, get_input
from html_parser import parse_title, parse_seasons, parse_episodes
from validator import validate_url, validate_path

def get_arguments():
    url = ""
    verbose = False
    file = ""

    parser = ArgumentParser()
    parser.add_argument("-u", "--url", dest="url", help="Searches the provided URL", metavar="URL")
    parser.add_argument("-v", "--verbose", dest="verbose", help="Enable verbose mode", action="store_true")
    parser.add_argument("-f", "--file", dest="file", help="FILE to save URLs to, if doesnt exist creates one", metavar="FILE")
    args = parser.parse_args()

    if args.url:
        url = args.url
    else:
        url = get_input("Enter URL")
        if not url:
            print("[red]URL is required![/red]")
            exit(1)
        if not validate_url(url):
            print("[red]Invalid URL![/red]")
            exit(1)

    if args.verbose:
        verbose = args.verbose

    if args.file:
        file = args.file
    else:
        file = get_input("Enter file to save URLs to")
        if not validate_path(file):
            print("[red]Invalid file![/red]")
            exit(1)
    
    return url, verbose, file

def main(args):
    if args[0]:
        if not validate_url(args[0]):
            print("[red]Invalid URL![/red]")
            return

    html = get_html(args[0])
    title = parse_title(html)
    seasons = parse_seasons(html)

    print("Searching [cyan bold]{}[/cyan bold]".format(title))

    if args[1]:
        print("Available Seasons:")
        for season, _ in seasons:
            print("[green]  {}[/green]".format(season))
    else:
        print("{} available seasons".format(len(seasons)))

    all_episodes = []

    for name, url in seasons:
        html = get_html(join_url(url))
        episodes = parse_episodes(html)
        print("[cyan bold]{}[/cyan bold] has [green bold]{}[/green bold] episodes".format(name, len(episodes)))
        if args[1]:
            for episode, _ in episodes:
                print("[green]  {}[/green]".format(episode))
        all_episodes.extend(episodes)

    if args[2]:
            print("Clearing [cyan bold]{}[/cyan bold]".format(args[2]))
            clear_file(args[2])
            print("Saving URLs to [cyan bold]{}[/cyan bold]".format(args[2]))
            for _, url in all_episodes:
                append_to_file(args[2], join_url(url))


if __name__ == "__main__":
    args = get_arguments()
    main(args)
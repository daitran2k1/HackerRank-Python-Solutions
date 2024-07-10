from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(tag)
        for attr in attrs:
            name, value = attr
            if value:
                print(f"-> {name} > {value}")
            else:
                print(f"-> {name} > None")

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        print(tag)
        for attr in attrs:
            name, value = attr
            if value:
                print(f"-> {name} > {value}")
            else:
                print(f"-> {name} > None")


if __name__ == "__main__":
    parser = MyHTMLParser()
    N = int(input())
    for _ in range(N):
        text = input()
        parser.feed(text)

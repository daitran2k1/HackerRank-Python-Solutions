from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, data: str) -> None:
        if "\n" in data:
            print(">>> Multi-line Comment")
            for comment in data.split("\n"):
                print(comment)
        else:
            print(">>> Single-line Comment")
            print(data)

    def handle_data(self, data: str) -> None:
        if data.strip():
            print(">>> Data")
            print(data)


if __name__ == "__main__":
    N = int(input())
    parser = MyHTMLParser()
    text = "\n".join(input() for _ in range(N))
    parser.feed(text)

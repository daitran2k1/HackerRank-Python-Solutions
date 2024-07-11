import xml.etree.ElementTree as etree

maxdepth = 0


def depth(elem: etree.Element, level: int):
    global maxdepth
    level += 1
    maxdepth = max(level, maxdepth)
    for child in elem:
        depth(child, level)


if __name__ == "__main__":
    N = int(input())
    xml = "\n".join([input() for _ in range(N)])
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

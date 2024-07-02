from collections.abc import Iterable

# I tried to do it in dict Comprehension, but I didn't how to add multi values to one key
def GropBy(f, items: Iterable):
    result = {}
    for item in items:
        result.setdefault(f(item), []).append(item)
    return result


if __name__ == '__main__':
    print(GropBy(len, ["hi", "bye", "yo", "try"]))


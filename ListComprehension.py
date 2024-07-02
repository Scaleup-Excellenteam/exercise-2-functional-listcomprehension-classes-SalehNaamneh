import wikipedia as wiki
def countWords(texts: str):
    ls = [word[:-1] if not word[-1].isalpha() else word for word in texts.split()]
    return {word: ls.count(word) for word in ls if word.isalpha()}


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(countWords(text))
    


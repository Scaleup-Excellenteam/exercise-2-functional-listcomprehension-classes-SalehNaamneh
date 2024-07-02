from PIL import Image

def PixelToWord(path: str) -> str:
    word = ""
    readImage = Image.open(path)
    readImage = readImage.convert("RGB")
    width, height = readImage.size
    for y in range(height):
        for x in range(width):
            r, g, b = readImage.getpixel((x, y))
            if r <= 1 and g <= 1 and b <= 1:
                # to get just the non-control chars like \n \r and something like this
                if 36 <= x <= 127:
                    word += chr(y)
    return word

if __name__ == '__main__':
    print(PixelToWord("C:\\Users\\Saleh\\Downloads\\code.png"))


from PIL import Image

def invert_image_colors(width, height):
    img = Image.new("RGB", (width, height), "white")
    pixels = img.load()

    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            pixels[x, y] = (255 - r, 255 - g, 255 - b)

    return img

if __name__ == "__main__":
    import time
    start = time.time()
    img = invert_image_colors(2000, 2000)
    end = time.time()
    print(f"Time taken: {end - start:.2f} seconds")
    img.save("inverted.png")

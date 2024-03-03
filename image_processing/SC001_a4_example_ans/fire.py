"""
File: fire.py
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, Import image path
    :return img: SimpleImage, Mark the picture of the fire area
    Function: Mark fire area
    Principle: Use mean value comparison to find the area with high R value and mark it out
    """
    img = SimpleImage(filename)
    for y in range(img.height):
        for x in range(img.width):
            pixel = img.get_pixel(x, y)
            grayscale = (pixel.red + pixel.green + pixel.blue) // 3
            if pixel.red > grayscale:
                pixel.red = 255
                pixel.green = 0
                pixel.blue = 0
            else:
                pixel.red = grayscale
                pixel.green = grayscale
                pixel.blue = grayscale
    return img


def main():
    """
    Function: Mark fire area
    Principle: Display the original picture and the special fire area picture
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()

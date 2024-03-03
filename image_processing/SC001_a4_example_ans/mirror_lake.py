"""
File: mirror_lake.py
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, Import image path
    :return new_img: SimpleImage, Export Mirror image
    Function: Mirror the original picture downward
    Principle: Symmetrically copy the RGB value of the original picture to achieve the mirror effect
    """
    img = SimpleImage(filename)

    new_img_height = img.height * 2
    new_img_width = img.width
    new_img = SimpleImage.blank(new_img_width, new_img_height)

    for y in range(img.height):
        for x in range(img.width):

            pixel = img.get_pixel(x, y)
            new_pixel1 = new_img.get_pixel(x, y)
            new_pixel2 = new_img.get_pixel(x, new_img_height-y-1)

            new_pixel1.red = pixel.red
            new_pixel1.green = pixel.green
            new_pixel1.blue = pixel.blue

            new_pixel2.red = pixel.red
            new_pixel2.green = pixel.green
            new_pixel2.blue = pixel.blue

    return new_img


def main():
    """
    Function: Mirror the original picture downward
    Principle: Display the original picture and the mirror picture
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()

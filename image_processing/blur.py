"""
File: blur.py
Name: Henry
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


BLUR_TIMES = 4
# Controls how many times we want to blur the image


def blur(img):
    """
    :param img: original image
    :return: blurred image
    """
    # Todo: create a new blank img that is as big as the original one
    new_img = SimpleImage.blank(img.width, img.height)
    # Loop over the picture
    for x in range(img.width):
        for y in range(img.height):
            # img_p = img.get_pixel(x, y)
            new_img_p = new_img.get_pixel(x, y)
            # Belows are 9 conditions of pixel filling, depending on pixels' x,y orientation.
            if x == 0 and y == 0:
                # Get pixel at the top-left corner of the image.
                r_avg = (img.get_pixel(1, 0).red + img.get_pixel(1, 1).red + img.get_pixel(0, 1).red) // 3
                g_avg = (img.get_pixel(1, 0).green + img.get_pixel(1, 1).green + img.get_pixel(0, 1).green) // 3
                b_avg = (img.get_pixel(1, 0).blue + img.get_pixel(1, 1).blue + img.get_pixel(0, 1).blue) // 3
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif x == img.width-1 and y == 0:
                # Get pixel at the top-right corner of the image.
                r_avg = (img.get_pixel(x-1, 0).red + img.get_pixel(x-1, 1).red + img.get_pixel(x, 1).red) // 3
                g_avg = (img.get_pixel(x-1, 0).green + img.get_pixel(x-1, 1).green + img.get_pixel(x, 1).green) // 3
                b_avg = (img.get_pixel(x-1, 0).blue + img.get_pixel(x-1, 1).blue + img.get_pixel(x, 1).blue) // 3
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif x == 0 and y == img.height-1:
                # Get pixel at the bottom-left corner of the image
                r_avg = (img.get_pixel(0, y-1).red + img.get_pixel(1, y-1).red + img.get_pixel(1, y).red) // 3
                g_avg = (img.get_pixel(0, y-1).green + img.get_pixel(1, y-1).green + img.get_pixel(1, y).green) // 3
                b_avg = (img.get_pixel(0, y-1).blue + img.get_pixel(1, y-1).blue + img.get_pixel(1, y).blue) // 3
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif x == img.width-1 and y == img.height-1:
                # Get pixel at the bottom-right corner of the image
                r_avg = (img.get_pixel(x, y-1).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x-1, y).red) // 3
                g_avg = (img.get_pixel(x, y-1).green + img.get_pixel(x-1, y-1).green + img.get_pixel(x-1, y).green) // 3
                b_avg = (img.get_pixel(x, y-1).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x-1, y).blue) // 3
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif 0 < x < img.width-1 and y == 0:
                # Get top edge's pixels (without two corners)
                r_avg = (img.get_pixel(x-1, 0).red + img.get_pixel(x-1, 1).red + img.get_pixel(x, 1).red
                         + img.get_pixel(x+1, 1).red + img.get_pixel(x+1, 0).red) // 5
                g_avg = (img.get_pixel(x-1, 0).green + img.get_pixel(x-1, 1).green + img.get_pixel(x, 1).green
                         + img.get_pixel(x+1, 1).green + img.get_pixel(x+1, 0).green) // 5
                b_avg = (img.get_pixel(x-1, 0).blue + img.get_pixel(x-1, 1).blue + img.get_pixel(x, 1).blue
                         + img.get_pixel(x+1, 1).blue + img.get_pixel(x+1, 0).blue) // 5
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif 0 < x < img.width-1 and y == img.height-1:
                # Get bottom edge's pixels (without two corners)
                r_avg = (img.get_pixel(x-1, y).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x, y-1).red
                         + img.get_pixel(x+1, y-1).red + img.get_pixel(x + 1, y).red) // 5
                g_avg = (img.get_pixel(x-1, y).green + img.get_pixel(x-1, y-1).green + img.get_pixel(x, y-1).green
                         + img.get_pixel(x+1, y-1).green + img.get_pixel(x+1, y).green) // 5
                b_avg = (img.get_pixel(x-1, y).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x, y-1).blue
                         + img.get_pixel(x+1, y-1).blue + img.get_pixel(x+1, y).blue) // 5
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif x == 0 and 0 < y < img.height-1:
                # Get left edge's pixels (without two corners)
                r_avg = (img.get_pixel(0, y-1).red + img.get_pixel(1, y-1).red + img.get_pixel(x+1, y).red
                         + img.get_pixel(x+1, y+1).red + img.get_pixel(0, y+1).red) // 5
                g_avg = (img.get_pixel(0, y-1).green + img.get_pixel(1, y-1).green + img.get_pixel(x+1, y).green
                         + img.get_pixel(x+1, y+1).green + img.get_pixel(0, y+1).green) // 5
                b_avg = (img.get_pixel(0, y-1).blue + img.get_pixel(1, y-1).blue + img.get_pixel(x+1, y).blue
                         + img.get_pixel(x+1, y+1).blue + img.get_pixel(0, y+1).blue) // 5
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            elif x == img.width-1 and 0 < y < img.height-1:
                # Get right edge's pixels (without two corners)
                r_avg = (img.get_pixel(x, y-1).red + img.get_pixel(x-1, y-1).red + img.get_pixel(x-1, y).red
                         + img.get_pixel(x-1, y+1).red + img.get_pixel(x, y+1).red) // 5
                g_avg = (img.get_pixel(x, y-1).green + img.get_pixel(x-1, y-1).green + img.get_pixel(x-1, y).green
                         + img.get_pixel(x-1, y+1).green + img.get_pixel(x, y+1).green) // 5
                b_avg = (img.get_pixel(x, y-1).blue + img.get_pixel(x-1, y-1).blue + img.get_pixel(x-1, y).blue
                         + img.get_pixel(x-1, y+1).blue + img.get_pixel(x, y+1).blue) // 5
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

            else:
                # Inner pixels.
                r_avg = (img.get_pixel(x-1, y-1).red + img.get_pixel(x, y-1).red + img.get_pixel(x+1, y-1).red
                         + img.get_pixel(x+1, y).red + img.get_pixel(x+1, y+1).red + img.get_pixel(x, y+1).red
                         + img.get_pixel(x-1, y+1).red + img.get_pixel(x-1, y).red) // 8
                g_avg = (img.get_pixel(x-1, y-1).green + img.get_pixel(x, y-1).green + img.get_pixel(x+1, y-1).green
                         + img.get_pixel(x+1, y).green + img.get_pixel(x+1, y+1).green + img.get_pixel(x, y+1).green
                         + img.get_pixel(x-1, y+1).green + img.get_pixel(x-1, y).green) // 8
                b_avg = (img.get_pixel(x-1, y-1).blue + img.get_pixel(x, y-1).blue + img.get_pixel(x+1, y-1).blue
                         + img.get_pixel(x+1, y).blue + img.get_pixel(x+1, y+1).blue + img.get_pixel(x, y+1).blue
                         + img.get_pixel(x-1, y+1).blue + img.get_pixel(x-1, y).blue) // 8
                new_img_p.red = r_avg
                new_img_p.green = g_avg
                new_img_p.blue = b_avg

    return new_img


def main():
    """
    TODO: Show 2 images: the original one and the blurred one of itself
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(BLUR_TIMES):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()

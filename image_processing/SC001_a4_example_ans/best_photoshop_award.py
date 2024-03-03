"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

THRESHOLD = 1.6
FIG_BLACK = 120
MOY_BLACK = 680
GLAS_BLACK = 700


def main():
    """
    Function: Picture of marriage notice
    Principle: Character + background, plus gold bars, and finally put on glasses
    """
    figure_img = SimpleImage("image_contest/NONO.jpg")
    background_img = SimpleImage("image_contest/BG.jpg")
    money_img = SimpleImage("image_contest/Money.jpg")
    glasses_img = SimpleImage("image_contest/Glasses.jpg")

    # First layer: combination of characters and background
    one_ps = photoshop_nono(figure_img, background_img)
    # Second layer: increase gold bars
    two_ps = photoshop_money(one_ps, money_img, 200, 500)
    for i in (320, 210, 100):
        two_ps = photoshop_money(two_ps, money_img, i, 610)
    for i in range(410, -10, -80):
        two_ps = photoshop_money(two_ps, money_img, i, 720)
    # Third layer: put on glasses
    three_ps = photoshop_glasses(two_ps, glasses_img, 248, 240)

    three_ps.show()


def photoshop_nono(figure_img, background_img):
    """
    Function: Combine characters and background
    :param figure_img: SimpleImage, Import figure picture
    :param background_img: SimpleImage, Import background image
    :return figure_img: SimpleImage, Export composite image
    """
    background_img.make_as_big_as(figure_img)

    for y in range(figure_img.height):
        for x in range(figure_img.width):
            fig_pixel = figure_img.get_pixel(x, y)
            bg_pixel = background_img.get_pixel(x, y)

            bigger = max(fig_pixel.red, fig_pixel.blue)
            total = fig_pixel.red + fig_pixel.green + fig_pixel.blue

            if fig_pixel.green > bigger * THRESHOLD and total > FIG_BLACK:
                fig_pixel.red = bg_pixel.red
                fig_pixel.green = bg_pixel.green
                fig_pixel.blue = bg_pixel.blue
    return figure_img


def photoshop_money(figure_img, money_img, x_piont, y_piont):
    """
    Function: Add gold bars to the picture
    :param figure_img: SimpleImage, Import original image
    :param money_img: SimpleImage, Import gold bar image
    :param x_piont: int, x coordinate
    :param y_piont: int, y coordinate
    :return figure_img: SimpleImage, Export composite image
    """
    for y in range(money_img.height):
        for x in range(money_img.width):
            fig_pixel = figure_img.get_pixel(x + x_piont, y + y_piont)
            moy_pixel = money_img.get_pixel(x, y)

            total = moy_pixel.red + moy_pixel.green + moy_pixel.blue
            if moy_pixel.red > moy_pixel.blue and total < MOY_BLACK:
                fig_pixel.red = moy_pixel.red
                fig_pixel.green = moy_pixel.green
                fig_pixel.blue = moy_pixel.blue
    return figure_img


def photoshop_glasses(figure_img, glasses_img, x_point, y_point):
    """
    Function: add glasses to the picture
    :param figure_img: SimpleImage, import original image
    :param glasses_img: SimpleImage, import glasses image
    :param x_point: int, x coordinate
    :param y_point: int, y coordinate
    :return figure_img: SimpleImage, export composite image
    """
    for y in range(glasses_img.height):
        for x in range(glasses_img.width):
            fig_pixel = figure_img.get_pixel(x + x_point, y + y_point)
            glasses_pixel = glasses_img.get_pixel(x, y)

            total = glasses_pixel.red + glasses_pixel.green + glasses_pixel.blue
            if total < GLAS_BLACK:
                fig_pixel.red = glasses_pixel.red
                fig_pixel.green = glasses_pixel.green
                fig_pixel.blue = glasses_pixel.blue
    return figure_img


if __name__ == '__main__':
    main()

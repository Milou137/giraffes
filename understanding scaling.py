# FROM
# https://stackoverflow.com/questions/43046376/how-to-change-an-image-size-in-pygame?rq=1
import sys
import pygame as pg


pg.init()
screen = pg.display.set_mode((640, 480))

IMAGE = pg.Surface((100, 60))
IMAGE.fill(pg.Color('sienna2'))
pg.draw.circle(IMAGE, pg.Color('royalblue2'), (50, 30), 20)
# New width and height will be (50, 30).
IMAGE_SMALL = pg.transform.scale(IMAGE, (50, 30))
# Rotate by 0 degrees, multiply size by 2.
IMAGE_BIG = pg.transform.rotozoom(IMAGE, 0, 2)


def main():
    clock = pg.time.Clock()
    done = False
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        screen.fill(pg.Color('gray15'))
        screen.blit(IMAGE, (50, 50))
        screen.blit(IMAGE_SMALL, (50, 155))
        screen.blit(IMAGE_BIG, (50, 230))
        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()
    sys.exit()

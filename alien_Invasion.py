import pygame
from settings import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group


def run_game():

    pygame.init()

    settings = Setting()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen, settings)

    bullets = Group()

    pygame.display.set_caption("Alien Invasion")

    while True:
        gf.check_event(settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(settings, screen, ship, bullets)


run_game()


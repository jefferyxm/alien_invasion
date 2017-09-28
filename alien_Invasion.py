import pygame
from settings import Setting
from ship import Ship
import game_function as gf
from pygame.sprite import Group
from game_stats import GameStats


def run_game():

    pygame.init()
    pygame.display.set_caption("Alien Invasion")

    settings = Setting()
    stats = GameStats(settings)
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    ship = Ship(screen, settings)

    bullets = Group()

    aliens = Group()

    gf.create_fleet(settings, screen, ship, aliens)

    while True:
        gf.check_event(settings, screen, ship, bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, ship, aliens, bullets)
            gf.update_aliens(settings, ship, aliens, screen, stats, bullets)
        gf.update_screen(settings, screen, ship, aliens, bullets)


run_game()


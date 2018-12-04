import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship

def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
   
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    
    #设置背景色
    bg_color = (230,230,230)
    #开始主循环
    while True:
        gf.check_events(ship)
        gf.update_screen(ai_settings,screen,ship)
        gf.check_events(ship)
        ship.update()
run_game()

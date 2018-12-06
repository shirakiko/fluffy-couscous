import sys
import pygame
import game_functions as gf
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from alien import Alien
def run_game():
    #初始化pygame、设置和屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height)) 
   
    pygame.display.set_caption("Alien Invasion")

    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个外星人
    alien = Alien(ai_settings,screen)
    #创建一个用于储存子弹的编组
    bullets = Group()
    #设置背景色
    bg_color = (230,230,230)
    #锁帧
    clock = pygame.time.Clock()
    #开始主循环
    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        gf.update_bullets(bullets)
        gf.update_screen(ai_settings,screen,ship,alien,bullets)
        ship.update()
        clock.tick(250)
        
        
run_game()

class Settings():
    """储存《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""

        #屏幕的设置、
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船的设置
        self.ship_speed_factor = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 19,26,81
        self.bullets_allowed = 3

        #外星人设置
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 1
        #fleet_direction为1表示向右移，为-1表向左移
        self.fleet_direction = 1

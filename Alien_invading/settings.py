class Settings():
    """储存《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的设置"""

        #屏幕的设置、
        self.screen_width = 1000
        self.screen_height = 600
        self.bg_color = (230,230,230)

        #飞船的速度
        self.ship_speed_factor = 1.5

        #子弹设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 19,26,81
        self.bullets_allowed = 3

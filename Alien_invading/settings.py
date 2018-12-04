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

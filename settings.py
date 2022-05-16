class Settings():
    """存储《外星人》的所有设置的类"""

    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕的设置
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (150,230,230)

        #飞船的设置
        self.ship_limit = 1

        #子弹的设置
        self.bullet_width = 1000
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullets_allowed = 3

        #游戏节奏
        self.speedup_scale = 1.5
        self.score_scale = 10

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化游戏设置"""
        self.ship_speed_factor = 1
        self.alien_speed_factor = 0.2
        self.bullet_speed_factor = 1
        self.fleet_drop_speed = 100
        # fleet_direction为1表示右移，-1表示左移
        self.fleet_direction = 1

        #记分
        self.alien_points = 50

    def increase_speed(self):
        """提高游戏难度"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        #让得分为整所以用int
        self.alien_points = int(self.alien_points * self.score_scale)

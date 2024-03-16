class Settings:
    #存储游戏《外星人入侵》中所有设置的类

    def __init__(self):
        #初始化游戏的设置
        #屏幕的设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.1

        #子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 8
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10

        #创建外星人群的初始数量
        self.ailen_numberr = 8
        self.ailen_numberc = 8
        #外星人设置
        self.alien_speed = 0.05
        self.fleet_drop_speed = 10
        # fleet_direction为 1 表示向右, 为 -1 表示向左移
        self.fleet_direction = 1

        #飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #加快游戏节奏的速度
        self.speedup_scale = 1.1
        #外星人分数提高速度
        self.socre_scale = 1.5

        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        #fleet_direction 为 1 表示向右, 为 -1 表示向左
        self.fleet_direction = 1
        #记分
        self.alien_points = 50
    def increase_speed(self):
        """"提高速度设置和外星人分数"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.socre_scale)
        #print(self.alien_points)

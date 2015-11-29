# -*- coding: utf-8 -*-

'''
Created on Nov 29, 2015

@author: luodichen
'''

class Weapon(object):
    def __init__(self,
                 name = None,                   # 武器名称
                 attack = 0,                    # 攻击力
                 defense = 0,                   # 防御力
                 affinity = 0,                  # 会心率
                 element1 = (None, 0),          # 属性 1, 属性与数值
                 element2 = (None, 0),          # 属性 2, 属性与数值
                 rarity = 1,                    # 稀有度
                 sharpness1 = [],               # 斩味
                 sharpness2 = [],               # 斩味 +1
                 slot = (False, False, False),  # 洞
                 children = []                  # 直接派生武器列表
                 ):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.affinity = affinity
        self.element1 = element1
        self.element2 = element2
        self.rarity = rarity
        self.sharpness1 = sharpness1
        self.sharpness2 = sharpness2
        self.slot = slot
        self.children = children

# -*- coding: utf-8 -*-

'''
Created on Nov 29, 2015

@author: luodichen
'''

# 武器基类, 所有武器共有的属性
class BaseWeapon(object):
    def __init__(self):
        self.name = None,                       # 武器名称
        self.attack = 0                         # 攻击力
        self.defense = 0                        # 防御力
        self.affinity = 0                       # 会心率
        self.rarity = 1                         # 稀有度
        self.slot = (False, False, False)       # 插槽
        self.children = []                      # 直接派武器列表

# 剑士武器
class Blademaster(BaseWeapon):
    def __init__(self):
        self.element = (None, 0, False)         # 属性效果 (属性, 数值, 是否需要觉醒发动)
        self.accumulation = (None, 0, False)    # 蓄積効果 (属性, 数值, 是否需要觉醒发动)
        self.length = 0                         # 斩味长度
        self.sharpness1 = []                    # 斩味
        self.sharpness2 = []                    # 斩味 +1

# 射手武器
class Gunner(BaseWeapon):
    pass

# 大剑
class GreatSword(Blademaster):
    pass

# 太刀
class LongSword(Blademaster):
    pass

# 片手剑
class Sword_n_Shield(Blademaster):
    pass

# 双剑
class DualBlades(Blademaster):
    def __init__(self):
        self.element2 = (None, 0, False)        # 属性效果 (属性, 数值, 是否需要觉醒发动)

# 大锤
class Hammer(Blademaster):
    pass

# 狩猎笛
class HutingHorn(Blademaster):
    def __init__(self):
        self.notes = []                         # 音色
        self.recital_notes = []                 # 旋律, [((音, 音, ..., 音), 技能), ..., ]

# 长枪
class Lance(Blademaster):
    pass

# 铳枪
class Gunlance(Blademaster):
    def __init__(self):
        self.shelling = None                    # 炮击

# 斩击斧
class SwitchAxe(Blademaster):
    def __init__(self):
        self.phial_type = None                  # 瓶类型

# 充能斧
class ChargeBlade(Blademaster):
    def __init__(self):
        self.phial_type = None                  # 瓶类型

# 操虫棍
class InsectGaive(Blademaster):
    def __init__(self):
        self.insect_type = None                 # 猎虫等级

# 轻弩
class LightBowgun(Gunner):
    pass

# 重弩
class HeavyBowgun(Gunner):
    pass

# 弓
class Bow(Gunner):
    pass

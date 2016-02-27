# -*- coding: utf-8 -*-
'''
Created on Dec 1, 2015

@author: Ling
'''

import urllib2
import re
from weapon import BaseWeapon
from pyquery import PyQuery

class WeaponFactory(object):
    '''
    classdocs
    '''


    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
        self.dict_handler = {u'名前': lambda node: node.text(),
                    u'攻撃力': lambda node: 0 if node.text() == '-' else int(str(node.text())),
                    u'防御力': lambda node: 0 if node.text() == '-' else int(str(node.text())),
                    u'会心率': lambda node: 0 if node.text() == '-' else int(node.text()[:-1]),
                    u'属性効果': self.handle_effect,
                    u'蓄積効果': self.handle_effect,
                    u'レア度': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'斬れ味長さ': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'斬れ味': self.handle_sharpness,
                    u'斬れ味+1': self.handle_sharpness,

                    u'スロット': self.handle_slot,

                    }
        
    def get_weapon(self):
        weapon = BaseWeapon()
        page = urllib2.urlopen(self.url).read()
        root = PyQuery(page)
        return self.get_baseweapon(root,weapon)

        
    def handle_effect(self, node):
        if node.text() == '-' :
            return None
        effect = [None, 0, False]
        text = node.text()
        if -1 == text.find(u'覚醒：'):
            effect[2] = True
            text = text[3:]
        pattern = re.compile(r'^(\D*)(\d*)$')
        m = pattern.match(text)
        effect[0] = m.group(1)
        effect[1] = int(m.group(2))
        return tuple(effect)
        
    def handle_sharpness(self, node):
        sharpness = []
        span = node("span")
        for i in xrange(len(span)-1):
            sharpness.append(len(span.eq(i).text()))
        return sharpness
            
    def handle_slot(self, node):

        return (u'○' == node.eq(i).text() for i in xrange(len(node.text())))

    ########## fresh start ##########


    
    def get_baseweapon(self, root, weapon):
        dict_tb = {}
        th = root(".t4 tr th")
        td = root(".t4 tr td")
        for i in xrange(len(th)):
            if not th.eq(i).text() in dict_tb:
                dict_tb[th.eq(i).text()] = self.dict_handler[th.eq(i).text()](td.eq(i))
        attr_dict = {'name': u'名前', 'attack': u'攻撃力', 'defense': u'防御力', 'affinity': u'会心率',
                     'element': u'属性効果', 'accumulation': u'蓄積効果'}
        for key in attr_dict:
            weapon.__setattr__(key, dict_tb[attr_dict[key]])
        return weapon
            
        

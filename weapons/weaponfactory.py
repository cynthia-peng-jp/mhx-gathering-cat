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
        
    def get_weapon(self):
        #weapon = Weapon()
        page = urllib2.urlopen(self.url).read()
        root = PyQuery(page)
        performance_left_table = root("table").eq(0)("td")
        attr_dict = {'name': 0, 'attack': 1, 'defense': 2, 'affinity': 3, 'element': 4, 'accumulation': 5}
        #for key in attr_dict:
        #    weapon.__setattr__(key, performance_left_table.eq(attr_dict[key]).text())
        #return weapon
        
    def handle_effect(self, node):
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
            
    dict_handler = {u'名前': lambda node: node.text(), 
                    u'攻撃力': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'防御力': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'会心率': lambda node: 0 if node.text() == '-' else int(node.text()[:-1]),
                    u'属性効果': handle_effect,
                    u'蓄積効果': handle_effect,
                    u'レア度': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'斬れ味長さ': lambda node: 0 if node.text() == '-' else int(node.text()),
                    u'斬れ味': handle_sharpness,
                    u'斬れ味+1': handle_sharpness,
                    
                    u'スロット': handle_slot,
                    
                    }
    
    def get_baseweapon(self, root, weapon):
        dict_tb = {}
        th = root("table").eq(0)("th")
        td = root("table").eq(0)("td")
        for i in xrange(len(th)):
            if not th.eq(i).text() in dict_tb:
                dict_tb[th.eq(i).text()] = td.eq(i).text()
            
        

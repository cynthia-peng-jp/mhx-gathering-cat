'''
Created on Dec 1, 2015

@author: Ling
'''
import urllib2
from weapon import Weapon
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
        weapon = Weapon()
        page = urllib2.urlopen(self.url).read()
        root = PyQuery(page)
        performance_left_table = root("table").eq(0)("td")
        attr_dict = {'name': 0, 'attack': 1, 'defense': 2, 'affinity': 3, 'element': 4, 'accumulation': 5}
        for key in attr_dict:
            weapon.__setattr__(key, performance_left_table.eq(attr_dict[key]).text())
            
        return weapon
    

# -*- coding: utf-8 -*-

import urllib2
from pyquery import PyQuery
from weaponfactory import WeaponFactory
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

### test 1 ###
# url = 'http://wiki.mh4g.org/data/1172.html'
# page = urllib2.urlopen(url).read()
# root = PyQuery(page)
# found = root("#tabledata tr[class!='sub_th'] td a")
# for i in xrange(len(found)):
#         print found.eq(i).text()
        
### test 2 ###
weaponfactory = WeaponFactory('http://wiki.mh4g.org/ida/131588.html').get_weapon()
print weaponfactory.name
print weaponfactory.slot


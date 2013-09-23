# -*- coding: utf-8 -*- 

'''
Created on 2013-9-23

@author: tuyun
'''

import urllib2
import json

from cityDict import city

def getWeatherByCityName(cityname):
    citycode = city.get(cityname)
    if citycode:
        url = ('http://www.weather.com.cn/data/cityinfo/%s.html' % citycode)
        content = urllib2.urlopen(url).read()
        data = json.loads(content)
        result = data['weatherinfo']
        str_tmp = ('%s\n%s~%s') % (result['weather'], result['temp1'], result['temp2'])
        return str_tmp
    
if __name__ == '__main__':
    cityname = raw_input('你想查询哪个城市的天气?\r\n')
    print getWeatherByCityName(cityname)
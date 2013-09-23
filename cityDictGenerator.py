# -*- coding: utf-8 -*- 

'''
Created on 2013-9-23

@author: tuyun
'''

fileHandle = open('city.txt', 'r') 
citysList = fileHandle.read() 
citys = citysList.split(',')
result = 'city = {\r\n'
for c in citys:
    city_entry = c.split(':')
    city_name = city_entry[0].strip()
    city_code = city_entry[1].strip()
    line = "'%s':'%s', \r\n" % (city_name, city_code)
    result += line
    
result +='}\r\n'
f=file('cityDict.py', 'w')
f.write('# -*- coding: utf-8 -*- ')
f.write('\r\n')
f.write(result)
fileHandle.close() 
f.close()
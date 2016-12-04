import re
from random import randint,choice

def show_insert(dup,source):
        airplanes = ['A300 ', 'A310 ', 'A310-600'  , 'A318' , 'A319 ' , 'A320 ' , 'A321', 'A321-100 ' , 'A321-200' , 'A330-220', 'CRJ', 'MD-11', 'MD-82', 'MD-90', 'A340-300', '737-700', '737-200', '737-200S ', '737-300' , '737-400   ', '747-SP ', '737-200  ', '747-400 ', '757-ALL', '767-300', '777-200', '777-ALL']
        airlines = re.compile(r'<div class="flex-card flex-listing flex-card-offer .*?>.*?<div class="flex-content">.*?<span class="departure-time.*?>(.+?)</span>.*?<span class="arrival-time.*?>(.+?)</span>.*?<div class="secondary" data-test-id="airports">(.+?)-(.+?)</div>.*?<span class="visuallyhidden">\$(.+?)<span',re.S)
        result = re.findall(airlines,source)

        for each in result:
                '''
                while True:
                        sand = randint(1000,9999)
                        if sand not in dup:
                                dup.append(sand)
                                break
                        else:
                                continue'''
                print(each)
		print('INSERT into flights values (%d,"%s","%s",%.2f,"2016-12-%d %s","%s");'%(sand,each[3],each[2],float(each[-1].replace(',','')),randint(1,31),each[0],choice(airplanes))
                













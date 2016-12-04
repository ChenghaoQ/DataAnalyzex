import re
from random import randint,choice
def show_insert(dup,source):




	airplanes = ['CRJ', 'MD-11', 'MD-82', 'MD-90', '154', '42', 'Yun-7', '146-300', '146', 'A310', 'A310-200', 'A300', 'A300-600', 'A310-300', 'A319', 'A320', 'A321', 'A330-200', 'A340', 'A340-300', '737-700', '737-200', '737-200', '737-200', '737-300', '737-400', '737-500', '737-600', '737', '737-800', '747-400', '747 SP', '747-200', '747-400', '747', '757', '767-300', '767-200', '777-200', '777']



	airlines = re.compile(r'<div class="flex-card flex-listing flex-card-offer .*?>.*?<div class="flex-content">.*?<span class="departure-time.*?>(.+?)</span>.*?<span class="arrival-time.*?>(.+?)</span>.*?<div class="secondary" data-test-id="airports">(.+?)-(.+?)</div>.*?<span class="visuallyhidden">\$(.+?)</span',re.S)   
	result = re.findall(airlines,source)
	for each in result:
                while True:
                        sand = randint(1000,9999)
                        if sand not in dup:
                                dup.append(sand)
                                break
                        else:
                                continue
                print('INSERT into Flights values (%d,"%s","%s",%.2f,"2016-12-%d %s","%s");'%(sand,each[3],each[2],float(each[-1].replace(',','')),randint(1,31),each[0],choice(airplanes)))


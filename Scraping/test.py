from urllib.request import urlopen
from bs4 import BeautifulSoup
from lxml import etree
#import pymongo
import csv
import requests
'''
fp=open('problemurl.csv','wt',newline='',encoding='utf-8')
writer=csv.writer(fp)
writer.writerow(('problem','url'))
client=pymongo.MongoClient('localhost',27017)
scraping=client['scraping']
problemurl=scraping['problemurl']
'''
headers={"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"
         ,"Cookie":'_zap=e2043cec-b379-4e6d-be45-b3b4b78239ce; d_c0="ALDXdZXs4RGPTjmba4sjEvKL1eAC5K4LdZc=|1599999289"; _ga=GA1.2.2008543628.1600008163; _xsrf=axuR8j7HvD3kW8aEHRNq50OK3ps4pb5j; q_c1=6595f1b472d74dcda4e95b349c8377cf|1605499059000|1605499059000; tst=h; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1605598067,1605598333,1605598519,1605598586; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1605598586; SESSIONID=8kTVfzDd90W39ys3EszewjLvhyBypiYrlteuILb1mEv; JOID=Ul0TCkr15yi20p0MMfzT_8gioOsmyI9z6LXiS1rN0nyK4-V6AY-WnODWmwA2b6r6GLSV0rxo8De4mLNdXAMSVJ0=; osd=U1gXBEz04iy41JwJNfLV_s0mru0nzYt97rTnT1TL03mO7eN7BIuYmuHTnw4wbq_-FrKU17hm9ja9nL1bXQYWWps=; capsion_ticket="2|1:0|10:1605598636|14:capsion_ticket|44:Mzg3MmY4YTQ5NTNlNGMxMjkzZjE0MjQ3NDAxNzgzNzk=|1035b0b79487aca5548a00d0e76c1e0c0bbc88ee81bb22047567a636aa55001c"; KLBRSID=d017ffedd50a8c265f0e648afe355952|1605598652|1605596830; z_c0="2|1:0|10:1605598652|4:z_c0|92:Mi4xZzBIOEJRQUFBQUFBc05kMWxlemhFU1lBQUFCZ0FsVk52TXVnWUFCUkV2UXdWVEQxMEhkZktLd2gzWlBkOF85cWNn|1784313e8ab65b1786e44b708e812fa89334d821cafa7c8f54e6df4e3d4f4a8d"; unlock_ticket="ABACW5evZgwmAAAAYAJVTcSEs1-Gl5pmZHRrL-6zKmJYe4YcIazSug=="'}
form_hot_url='https://www.zhihu.com/search?type=content&q='
hot_str=['数学','化学','计算机','经济','物理','生物','能力','自杀','美好','语文','商品','如何做','怎么办','零食','人工智能']
for hs in hot_str:
    hurl=form_hot_url+hs
    hres = requests.get(hurl, headers=headers)
    print(hres.text)
    break
    '''
    hselector = etree.HTML(hres.text)
    for i in range(2,51):
        hpath1='/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/h2/div/meta[1]'
        #/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div[2]/div/div/h2/div/meta[1]
        #/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div[3]/div/div/h2/div/meta[1]
        #/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div[26]/div/div/h2/div/meta[1]
        id1=hselector.xpath(hpath1)
        print(id1)
        
        question=id1[0].split('/')
        hpath2='/html/body/div[1]/div/main/div/div[2]/div[2]/div/div/div/div/div['+str(i)+']/div/div/h2/div/meta[2]/@content'
        text1=hselector.xpath(hpath2)
        if 'question'in question and 'zvideo'not in question and id1[0] not in problem[0]:
            problem=[text1[0],id1[0]]
#soup=BeautifulSoup(res.text,'html.parser')
            print(problem)
#print(id2)
#print(soup)

'''
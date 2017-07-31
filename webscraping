import json
import math
import requests
from bs4 import BeautifulSoup

house591 = requests.get("https://newhouse.591.com.tw/housing-list.html?rid=1&sids=0")
content591 = house591.content
soup591 = BeautifulSoup(content591,"html.parser")
house_sum = soup591.find('span',{"class":"fc-red"})
pages = math.ceil(int(house_sum.text)/12)

house_list = []
base_url = "https://newhouse.591.com.tw/index.php?firstRow="
for page in range(0,pages*12,12):
    house = requests.get(base_url + str(page) + "&totalRows=" + house_sum.text + "&rid=1&module=housing&action=list")
    house_soup = BeautifulSoup(house.content, "html.parser")
    house_all = house_soup.find_all('li',{"class":"detailItemBox clearfix "})
    for item in house_all:
        house_dict = {}
        try:
            house_dict['houseName'] = item.find('p',{"class","houseName"}).find('a').text
        except:
            house_dict['houseName'] = None
        try:
            address = item.find('p',{"class","address"}).find('a').text
            end = address.find('(')
            if end == (-1):
                end = address.rfind('號')
                if end == (-1):
                    house_dict['address'] = address
                else:
                    house_dict['address'] = address[0:end+1]
            else:
                house_dict['address'] = address[0:end]
        except:
            house_dict['address'] = None
        try:
            house_dict['averPrice'] = item.find('p',{"class","averPrice"}).find('em').text
        except:
            house_dict['averPrice'] = None

        house_list.append(house_dict)
        print(house_list)

with open('houses.json', 'w', encoding='utf-8') as file:
    json.dump(house_list, file, ensure_ascii=False)
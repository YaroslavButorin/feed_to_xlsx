import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
import xmltodict, json
import os
from lxml import etree
import xlsxwriter
import xml.etree.ElementTree as et
filename = 'ozon.xml'

with open(filename, "rb") as f:
    contents = f.read().decode("UTF-8")
soup = BeautifulSoup(contents, 'html.parser')

offer = []

for a in soup.find_all('offer'):
    print(a['id'])
    all_tag_name = [x.name for x in a.find_all() if x.name != 'param']
    all_tag_val = [x.text for x in a.find_all() if x.name != 'param']
    pic_all = [x.text for x in a.find_all() if x.name == 'picture']
    pic_all = '\n'.join(str(e) for e in pic_all)
    pic_all = {'all_pic':pic_all}
    dict_offer = dict(zip(all_tag_name,all_tag_val))
    param_name = [x['name'] for x in a.find_all() if x.name == 'param']
    param_val = [x.next.strip() for x in a.find_all() if x.name == 'param']
    dict_offer_param = dict(zip(param_name,param_val))
    dict_offer.update(dict_offer_param)
    dict_offer.update(pic_all)
    offer.append(dict_offer)

df = pd.DataFrame(offer)
df = df.fillna('')

df.to_excel('goods.xlsx',index=True)
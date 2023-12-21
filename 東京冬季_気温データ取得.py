from bs4 import BeautifulSoup
from time import sleep
import requests
import pandas as pd

url = 'https://www.data.jma.go.jp/obd/stats/etrn/view/nml_sfc_d.php?prec_no=44&block_no=47662&year=&month={}&day=&view=a2'

#空のリスト
temp_list = []

#11月の気温取得
url_Nov = url.format(11)

r_Nov = requests.get(url_Nov)

sleep(1)

soup_Nov = BeautifulSoup(r_Nov.text, 'lxml')

#11月の表取得
Table_Nov = soup_Nov.find('table', class_='data2_s')

#11月の日付毎の温度
days_Nov = Table_Nov.find_all('tr', style='text-align:center')

#17日から30日の気温取得
for day_Nov in days_Nov[16:30]:
    #それぞれの日にちの8時から20時の気温取得
    temps_Nov = day_Nov.find_all('td', style='text-align:right')[10:23]
    for temp_Nov in temps_Nov:
        temp_list.append(temp_Nov.text)

#12月の気温取得
url_Dec = url.format(12)

r_Dec = requests.get(url_Dec)

sleep(1)

soup_Dec = BeautifulSoup(r_Dec.text, 'lxml')

#12月の表取得
Table_Dec = soup_Dec.find('table', class_='data2_s')

#12月の日付毎の温度
days_Dec = Table_Dec.find_all('tr', style='text-align:center')

#1日から31日の気温取得
for day_Dec in days_Dec[0:31]:
    #それぞれの日にちの8時から20時の気温取得
    temps_Dec = day_Dec.find_all('td', style='text-align:right')[10:23]
    for temp_Dec in temps_Dec:
        temp_list.append(temp_Dec.text)

#1~3月の気温取得
for i in range(1, 4):
    #i月のurl取得
    url_i = url.format(i)

    r_i = requests.get(url_i)

    sleep(1)

    soup_i = BeautifulSoup(r_i.text, 'lxml')

    #i月の表取得
    Table_i = soup_i.find('table', class_='data2_s')
    
    #i月の日付毎の温度
    days_i = Table_i.find_all('tr', style='text-align:center')

    #一月30日の時と31日の時で場合分け
    if days_i==30:
        for day_i in days_i[0:30]:
            temps_i = day_i.find_all('td', style='text-align:right')[10:23]
            for temp_i in temps_i:
                temp_list.append(temp_i.text)
    else:
        for day_i in days_i[0:31]:
            temps_i = day_i.find_all('td', style='text-align:right')[10:23]
            for temp_i in temps_i:
                temp_list.append(temp_i.text)

#4月の気温取得
url_Apr = url.format(4)

r_Apr = requests.get(url_Apr)

sleep(1)

soup_Apr = BeautifulSoup(r_Apr.text, 'lxml')

#4月の表取得
Table_Apr = soup_Apr.find('table', class_='data2_s')

#4月の日付毎の温度
days_Apr = Table_Apr.find_all('tr', style='text-align:center')

for day_Apr in days_Apr[0:3]:
    temps_Apr = day_Apr.find_all('td', style='text-align:right')[10:23]
    for temp_Apr in temps_Apr:
        temp_list.append(temp_Apr.text)



df = pd.DataFrame(temp_list)
#csvで保存
df.to_csv('平年値冬季.csv', index=None, encoding='utf-8-sig')

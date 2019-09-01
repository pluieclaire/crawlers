import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
#browser = webdriver.Chrome('BrowserDriverPath')

path = "C:\pro\driver\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('headless')
#options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
driver = webdriver.Chrome(path, chrome_options=options)
#driver = webdriver.Chrome(path)
ref = [
    ('지구한바퀴_세계여행', 'travel'),
    ('시사·이슈', 'sisa'),
    ('IT_트렌드', 'it'),
    ('사진·촬영', 'photo'),
    ('취향저격_영화_리뷰', 'movie'),
    ('오늘은_이런_책', 'book'),
    ('뮤직_인사이드', 'music'),
    ('글쓰기_코치', 'write'),
    ('직장인_현실_조언', 'work'),
    ('스타트업_경험담', 'startup'),
    ('육아_이야기', 'kid'),
    ('요리·레시피', 'cook'),
    ('건강·운동', 'health'),
    ('멘탈_관리_심리_탐구', 'psy'),
    ('디자인_스토리', 'design'),
    ('문화·예술', 'art'),
    ('건축·설계', 'arch'),
    ('인문학·철학', 'hum'),
    ('쉽게_읽는_역사', 'his'),
    ('우리집_반려동물', 'pet'),
    ('사랑·이별', 'love'),
    ('감성_에세이', 'esc')
]

if not os.path.isfile('./data/brunch/brucn_urls.csv'):
    keys_to_csv = [
        ['지구한바퀴_세계여행', 'travel'],
        ['시사·이슈', 'sisa'],
        ['IT_트렌드', 'it'],
        ['사진·촬영', 'photo'],
        ['취향저격_영화_리뷰', 'movie'],
        ['오늘은_이런_책', 'book'],
        ['뮤직_인사이드', 'music'],
        ['글쓰기_코치', 'write'],
        ['직장인_현실_조언', 'work'],
        ['스타트업_경험담', 'startup'],
        ['육아_이야기', 'kid'],
        ['요리·레시피', 'cook'],
        ['건강·운동', 'health'],
        ['멘탈_관리_심리_탐구', 'psy'],
        ['디자인_스토리', 'design'],
        ['문화·예술', 'art'],
        ['건축·설계', 'arch'],
        ['인문학·철학', 'hum'],
        ['쉽게_읽는_역사', 'his'],
        ['우리집_반려동물', 'pet'],
        ['사랑·이별', 'love'],
        ['감성_에세이', 'esc']
    ]

    df = pd.DataFrame(keys_to_csv, dtype='object')
    df.to_csv('./data/brunch/brunch_urls.csv', index=False, mode='a', header=False)

data = pd.read_csv("./data/brunch/brunch_urls.csv", names=["key", "theme"], sep=",", dtype='object')
total_rows = data.shape[0]

for i in range(total_rows):
    key = data['key'][i]
    url = f'https://brunch.co.kr/keyword/{key}?q=g'
    driver.get(url)
    time.sleep(1)

    elem = driver.find_element_by_tag_name("body")
    no_of_pagedowns = 5000

    while no_of_pagedowns > 0:
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
        no_of_pagedowns -= 1
        print(no_of_pagedowns)
        #date = driver.find_element_by_class_name("publish_time").text
        #if date.endswith('2019'):
        #    break
    
    article_urls = driver.find_elements_by_class_name("link_post")
    
    url_list = []
    for article_url in article_urls:
        href = article_url.get_attribute("href")
        #print(href)
        url_list.append(href)

    df = pd.DataFrame(url_list, dtype='object')
    df.to_csv('./data/brunch/brunch_{}.csv'.format(data['theme'][i]), index=False, mode='a', header=False)

    data = data.drop(i,0)
    data.to_csv('./data/brunch/brunch_urls.csv', index=False, mode='w', header=False)
    



    
import time
import csv
from selenium import webdriver
driver = webdriver.Chrome()
data_list = []
driver.get('https://www.endata.com.cn/BoxOffice/MovieStock/movies.html')
tags = driver.find_element_by_id('ulcontent').find_elements_by_tag_name('li')
for tag in tags:
    image_href = tag.find_element_by_tag_name('img').get_attribute('src')
    detail_href = tag.find_element_by_tag_name('a').get_attribute('href')
    text_tag = tag.find_element_by_class_name('info')
    c_name = text_tag.find_element_by_tag_name('a').text
    other_info = tag.find_elements_by_tag_name('p')
    e_name = other_info[0].text
    box_office = other_info[1].text[4:-1]
    info_dict = {
        '中文名':c_name,
        '英文名':e_name,
        '封面链接':image_href,
        '详情页链接':detail_href,
        '票房':box_office
    }
    print(info_dict)
    data_list.append(info_dict)
time.sleep(3)
driver.quit()
with open('E:\python\Python爬虫\爬取的信息\CSV/恩艺电影.csv','w',encoding='utf-8-sig')as f:
    f_csv = csv.DictWriter(f,fieldnames=['中文名','英文名','封面链接','详情页链接','票房'])
    f_csv.writeheader()
    f_csv.writerows(data_list)
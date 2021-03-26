'''
按关键词搜索评分大于 0 的豆瓣图书
'''

import sys
import re
import json
from selenium import webdriver

SEARCH_URL = "https://search.douban.com/book/subject_search"
SEARCH_TEXT = sys.argv[1]

def search(start, collect):
    if start > 250:
        return

    driver.get(SEARCH_URL + f'?search_text={SEARCH_TEXT}&start={start}')

    item_list = driver.find_elements_by_class_name('sc-bZQynM')
    item_len = len(item_list)
    if item_len == 0:
        return
    
    for item in item_list:
        try:
            rating = item.find_element_by_class_name('rating_nums')
        except Exception:
            continue

        title = item.find_element_by_class_name('title-text')
        link = title.get_attribute('href')
        people = re.search('\d+', item.find_element_by_class_name('pl').text).group()
        cover = item.find_element_by_class_name('cover').get_attribute('src')

        collect.append({
            'title':  title.text,
            'link':   link,
            'rating': float(rating.text),
            'people': int(people),
            'cover':  cover,
        })
    
    search(start + item_len, collect)

with webdriver.Chrome() as driver:
    books = []
    search(0, books)
    print(json.dumps(books, ensure_ascii=False))

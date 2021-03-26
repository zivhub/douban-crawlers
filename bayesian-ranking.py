'''
按贝叶斯平均分对图书进行排序
'''

import sys
import json

def sort_by_bayesian(book):
    return book['bayesian']

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    books = json.loads(f.read())

num_books = len(books)
whole_score = 0
whole_people = 0
for book in books:
    whole_score += book['rating'] * book['people']
    whole_people += book['people']

for book in books:
    book['bayesian'] = (whole_score + book['rating'] * book['people'] * num_books) / (whole_people + book['people'] * num_books)

books.sort(key=sort_by_bayesian, reverse=True)

print(json.dumps(books, ensure_ascii=False))

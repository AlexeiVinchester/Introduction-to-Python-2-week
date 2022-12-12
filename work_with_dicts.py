import operator


check_text = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

"""Задание"""
"""Подсчитаем 3 самых часто используемых слова и выведем их на экран"""

all_words = dict()

for word in check_text.split():
    cleaned_word = word.strip(',.!-/').lower()
    if cleaned_word not in all_words:
        all_words[cleaned_word] = 0
    all_words[cleaned_word] += 1

#создадим список кортежей из словаря
words_tuples = all_words.items()
word_count = sorted(words_tuples, key=operator.itemgetter(1), reverse=True)
three_most_common_words = word_count[:3]
print(three_most_common_words)

#Данную задачу можно решить и быстрее
from collections import Counter

cleaned_list = list()
for word in check_text.split():
    cleaned_list.append(word.strip(',.!*-').lower())
sorted_most_common_list = Counter(cleaned_list).most_common(3)
print(sorted_most_common_list)
adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""


adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")


# task 02 ==
""" Замініть .... на пробіл
"""


adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")


# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""


import re
adwentures_of_tom_sawer = re.sub(r'\s+', ' ', adwentures_of_tom_sawer).strip()


# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""


h_count = adwentures_of_tom_sawer.count('h')
print("Task 4:", h_count)


# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""


words = adwentures_of_tom_sawer.split()
bid_letters = sum(1 for word in words if word and word[0].isupper())
print("Task 5:", bid_letters)


# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""


first_tom_index = adwentures_of_tom_sawer.find('Tom')
second_tom_index = adwentures_of_tom_sawer.find('Tom', first_tom_index + 1)
print("Task 6:", second_tom_index)


# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""


adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')


# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""


if len(adwentures_of_tom_sawer_sentences) >= 4:
    fourth_sentence = adwentures_of_tom_sawer_sentences[3].strip().lower()
    print("Task 8:", fourth_sentence)


# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""


by_the_time = any(sentence.strip().startswith("By the time") for sentence in adwentures_of_tom_sawer_sentences)
print("Task 9:", by_the_time)


# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""


if adwentures_of_tom_sawer_sentences[-1].strip():
    last_sentence_words = adwentures_of_tom_sawer_sentences[-1].strip().split()
else:
    last_sentence_words = adwentures_of_tom_sawer_sentences[-2].strip().split()
print("Task 10:", len(last_sentence_words))
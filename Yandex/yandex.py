massive = (str(input('Введите слова через пробел, по окончании ввода нaжмите Enter: ')))
# print(massive)
a = massive.split()
# print(a)

a_set = set(a)

most_repeatable = None
rep_most_repeatable = 0

for item in a_set:
    rep = a.count(item)
    if rep > rep_most_repeatable:
        rep_most_repeatable = rep
        most_repeatable = item

print(most_repeatable)

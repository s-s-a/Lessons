# Ситуации, в которых полезно использовать словарь

s = input()
d = {}

for i in s:
    if i.isalpha():
        # d[i] = 1 if i not in d else d[i]+1
        d[i] = d.get(i, 0) + 1

for i in sorted(d):
    print(i, d[i])
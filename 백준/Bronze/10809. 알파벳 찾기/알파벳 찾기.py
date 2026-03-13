import string
S = input()
lower = [i for i in string.ascii_lowercase]
for i in lower:
    print(S.find(i), end = ' ')
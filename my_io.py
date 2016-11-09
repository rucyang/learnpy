#! /usr/bin/env python3
# ! -*- coding:utf-8 -*-
try:
    f = open('readme.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()

print('#########################')

with open('readme.txt', 'rb') as f:
    L = f.read().decode("utf8")

print(L)

# for line in L:
#     print line.strip()

# for i in range(len(L)):

#     L[i] = L[i].strip()

# for i in range(len(L)):
#     L[i] = L[i][:-1]
print(L)

print("##########################")

with open('thumb.jpg', "rb") as f1:
    print(f1.read())

with open("readme.txt", 'w') as f1:
    f1.write('你是我的眼！')

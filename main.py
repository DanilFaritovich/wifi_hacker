from itertools import combinations_with_replacement

i = [chr(i) for i in range(33, 127)]


# i.extend([chr(i) for i in range(1040, 1104)])

def worker(list1, list2):
    return [text1 + text2
            for text1 in list1
            for text2 in list2]


# b = worker(i, i)
# for n in range(2):
#    print(b)
#    b = worker(b, i)
res = [''.join(t) for t in combinations_with_replacement(i, 2)]
print(res)
res.extend(i)
res = [''.join(t) for t in combinations_with_replacement(res, 2)]
print(res)
res.extend(i)
res = [''.join(t) for t in combinations_with_replacement(res, 2)]
print(res)

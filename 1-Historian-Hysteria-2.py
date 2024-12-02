from collections import Counter

list1, list2 = [], []

with open('1-input', 'r') as f:
    for line in f:
        a, b = list(map(lambda x: int(x), line.split('   ')))
        list1.append(a)
        list2.append(b)

counter = Counter(list2)

sum = 0
for num in list1:
    num2 = counter.get(num, 0)
    sum += num * num2

print(sum)

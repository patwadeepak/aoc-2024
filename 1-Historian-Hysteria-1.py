list1, list2 = [], []

with open('1-input', 'r') as f:
    for line in f:
        a, b = list(map(lambda x: int(x), line.split('   ')))
        list1.append(a)
        list2.append(b)

list1.sort()
list2.sort()

sum = 0
for a, b in zip(list1, list2):
    sum += abs(a-b)

print(sum)

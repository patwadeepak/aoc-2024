import itertools
lines = []
with open("7-input", "r") as f:
    for line in f:
        lines.append(line.replace('\n', ''))

def concat(x, y):
    return int(str(x)+str(y))

l = [int.__add__, int.__mul__, concat]
getops = lambda n: list(itertools.product(l, repeat=n))

total = 0
for line in lines:
    r, nums = line.split(': ')
    r = int(r)
    nums = list(map(int, nums.split(' ')))

    ops = getops(len(nums)-1)
    is_ok = False
    for op_set in ops:
        k = 1
        pr = nums[0]
        for op in op_set:
            pr = op(pr, nums[k])
            k += 1
        if r == pr:
            is_ok = True
            break

    if is_ok:
        total += r

print(total)
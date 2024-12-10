def get_bin_string(n, max_n):
    max_n_len = len(str(bin(max_n-1)).lstrip('0b'))
    return str(bin(n)).lstrip('0b').zfill(max_n_len)

def get_operator(string):
    if string == '1':
        return int.__add__
    else:
        return int.__mul__

lines = []
with open('7-input', 'r') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

total = 0
for line in lines:
    result, nums = line.split(': ')
    result = int(result)
    nums = list(map(int, nums.split(' ')))

    n = 2**(len(nums) - 1)

    is_correct = False
    for i in range(n):
        bin_string = get_bin_string(i, n)

        k = 1
        s = nums[0]
        for op in bin_string:
            operator = get_operator(op)
            s = operator(s, nums[k])
            k += 1
        
        if result == s:
            is_correct = True
            break
    
    if is_correct:
        total += result

print(total)

import re

valid_instructions = []
with open('3-input', 'r') as f:
    for line in f:
        instructions = re.findall('mul\(\d{1,3},\d{1,3}\)', line)
        valid_instructions.extend(instructions)

sum = 0

for i in valid_instructions:
    a, b = list(map(int, i[4:-1].split(',')))
    sum += a*b

print(sum)

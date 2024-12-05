import re

def get_xmas_count(lines):
    total = 0
    for line in lines:
        all_xmas = re.findall('XMAS', line)
        all_smax = re.findall('SAMX', line)
        total += len(all_xmas) + len(all_smax)
    return total

total_xmas = 0
lines = []
n = None
with open('4-input', 'r') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

n = len(lines)
vlines = ['']*n
diag1 = ['']*(2*n - 1)
diag2 = ['']*(2*n - 1)

for i, line in enumerate(lines):
    for j, ch in enumerate(line):
        vlines[j] += ch
        diag1[i + j] += ch

    for k, ch in enumerate(line[::-1]):
        diag2[i + k] += ch

total_xmas = list(map(get_xmas_count, [lines, vlines, diag1, diag2]))

print(sum(total_xmas))

total_xmas = 0
lines = []

with open('4-input', 'r') as f:
    for line in f:
        lines.append(line.replace('\n', ''))

for i, line in enumerate(lines[1:-1], start=1):
    for j, ch in enumerate(line[1:-1], start=1):
        if ch == 'A':
            if ((lines[i-1][j-1] == 'M' and lines[i+1][j+1] == 'S') \
                or (lines[i-1][j-1] == 'S' and lines[i+1][j+1] == 'M')) and \
               ((lines[i+1][j-1] == 'M' and lines[i-1][j+1] == 'S') \
                or (lines[i+1][j-1] == 'S' and lines[i-1][j+1] == 'M')):
                total_xmas += 1

print(total_xmas)

updates, rules = [], []

with open('5-input', 'r') as f:
    reading_page_updates = False
    for line in f:
        if line == '\n':
            reading_page_updates = True
            continue
        if reading_page_updates:
            updates.append(line.replace('\n', ''))
        else:
            rules.append(line.replace('\n', ''))


rules_map = {}
for rule in rules:
    a, b = list(map(int, rule.split('|')))
    if b in rules_map:
        rules_map[b].add(a)
    else:
        rules_map[b] = set([a])

middle_sum = 0
for k, update in enumerate(updates):
    update = list(map(int, update.split(',')))
    is_valid = True
    for i, page in enumerate(update):
        if page in rules_map:
            violations = rules_map[page] & set(update[i+1:])
            if len(violations) > 0:
                is_valid = False
                break

    if is_valid:
        middle_sum += update[int((len(update)-1)/2)]

print(middle_sum)

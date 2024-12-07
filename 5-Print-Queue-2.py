def bubble_sort(arr, compare):
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  
        for i in range(n):
            if compare(arr[i], arr[i + 1]):
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        if not swapped:
            break

rules, updates = [], []

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

graph = {}
for rule in rules:
    a, b = list(map(int, rule.split('|')))
    if a in graph:
        graph[a].add(b)
    else:
        graph[a] = set([b])

all_nums = set([])
for k, v in graph.items():
    all_nums.add(k)
    all_nums = all_nums | v

list_all_nums = list(all_nums)

def compare(x, y):
    if x in graph:
        if y in graph[x]:
            return False
        else:
            return True

    if y in graph:
        if x in graph[y]:
            return True
        else:
            return False

bubble_sort(list_all_nums, compare)

sum_valid = 0
sum_invalid = 0
for i, update in enumerate(updates):
    update = list(map(int, update.split(',')))
    index_list = []

    is_valid = False

    before = ','.join(map(str, update))
    corrected_update = update.copy()
    bubble_sort(corrected_update, compare)
    after = ','.join(map(str, corrected_update))
    is_valid = before == after
    if not is_valid:
        sum_invalid += corrected_update[int((len(corrected_update)-1)/2)]
    else:
        sum += update[int((len(update)-1)/2)]

print(sum_valid, ',', sum_invalid)

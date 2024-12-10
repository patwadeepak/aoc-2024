actual_map = []
start_pos = None
with open('6-input', 'r') as f:
    for line in f:
        actual_map.append(list(line.replace('\n', '')))
        j = line.find('^')
        if line.find('^') != -1:
            start_pos = [len(actual_map)-1, j]

LOOP_THRESHOLD = 1000 # this takes 40s to run for me.

def is_gaurd_in_loop(graph):
    pos = start_pos.copy()
    guard_pos = set()
    repeat = 0
    is_loop = False
    while True:
        if tuple(pos) in guard_pos:
            repeat += 1
            if repeat > LOOP_THRESHOLD:
                is_loop = True
                break
        guard_pos.add(tuple(pos))

        if graph[pos[0]][pos[1]] == '^':
            if 0 > pos[0] - 1:
                break
            if graph[pos[0] - 1][pos[1]] == '#':
                graph[pos[0]][pos[1]] = '>'
            else:
                graph[pos[0]][pos[1]] = '.'
                pos[0] -= 1
                graph[pos[0]][pos[1]] = '^'

        if graph[pos[0]][pos[1]] == '>':
            if pos[1] + 1 >= len(graph):
                break
            if graph[pos[0]][pos[1] + 1] == '#':
                graph[pos[0]][pos[1]] = 'v'
            else:
                graph[pos[0]][pos[1]] = '.'
                pos[1] += 1
                graph[pos[0]][pos[1]] = '>'

        if graph[pos[0]][pos[1]] == 'v':
            if pos[0] + 1 >= len(graph):
                break
            if graph[pos[0] + 1][pos[1]] == '#':
                graph[pos[0]][pos[1]] = '<'
            else:
                graph[pos[0]][pos[1]] = '.'
                pos[0] += 1
                graph[pos[0]][pos[1]] = 'v'

        if graph[pos[0]][pos[1]] == '<':
            if 0 > pos[1] - 1:
                break
            if graph[pos[0]][pos[1] - 1] == '#':
                graph[pos[0]][pos[1]] = '^'
            else:
                graph[pos[0]][pos[1]] = '.'
                pos[1] -= 1
                graph[pos[0]][pos[1]] = '<'

    return is_loop

possible_loop = 0
for i, line in enumerate(actual_map):
    for j, point in enumerate(line):
        if actual_map[i][j] == '.':
            modified_graph = [x.copy() for x in actual_map]
            modified_graph[i][j] = '#'
            is_looped = is_gaurd_in_loop(modified_graph)
            if is_looped:
                possible_loop += 1

print(possible_loop)

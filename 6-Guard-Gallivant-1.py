actual_map = []
start_pos = None

with open('6-input', 'r') as f:
    for line in f:
        actual_map.append(list(line.replace('\n', '')))
        j = line.find('^')
        if line.find('^') != -1:
            start_pos = [len(actual_map)-1, j]

def get_all_guard_positions(graph):
    pos = start_pos.copy()
    guard_pos = set()

    while True:
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

    return len(guard_pos)

print(get_all_guard_positions(actual_map))

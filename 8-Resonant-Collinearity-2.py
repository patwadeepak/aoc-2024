import itertools

chars = {}
N = None

getpairs = lambda l, n: list(itertools.combinations(l, n))

def make_complex(t):
    return complex(t[0], t[1])

def is_inside(point):
    return 0 <= point.real <= N-1 and 0 <= point.imag <= N-1

with open('8-input', 'r') as file:
    i = 0
    for line in file:
        N = len(line)
        for j, ch in enumerate(line):
            if ch == '.' or ch == '\n':
                continue
            if ch in chars:
                chars[ch].add((i,j))
            else:
                chars[ch] = set([(i,j)])
        i += 1

an_set = set()
for char, sets in chars.items():
    temp_set = set()
    pairs = getpairs(sets, 2)
    for pair in pairs:
        a, b = make_complex(pair[0]), make_complex(pair[1])

        d = a - b

        is_in = True
        i = 0
        while is_in:
            p1 = a + d*i
            if is_inside(p1):
                an_set.add(p1)
            else:
                is_in = False
            i += 1

        is_in = True
        i = 0
        while is_in:
            p2 = b - d*i
            if is_inside(p2):
                an_set.add(p2)
            else:
                is_in = False
            i += 1

an = len(an_set)
print('Number of Anitnodes: ', an)

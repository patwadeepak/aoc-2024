def check_validity(report):
    is_valid = True
    trend = None
    for i, num in enumerate(report[1:], start=1):
        prev = report[i-1]
        diff = abs(prev-num)
        if diff <= 3 and diff >= 1:
            pass
        else:
            is_valid = False
            break

        if trend is not None:
            # check trend change then
            new_trend = (prev-num)/abs(prev-num)
            if new_trend + trend == 0:
                is_valid = False
                break
        else:
            trend = (prev-num)/abs(prev-num)

    return is_valid
        
sum = 0
with open('2-Red-Nosed-Reports', 'r') as f:
    for line in f:
        report = list(map(lambda x: int(x), line.split(' ')))
        is_valid = check_validity(report)

        if is_valid:
            sum += 1

print(sum)
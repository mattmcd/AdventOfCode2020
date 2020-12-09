def read(s=None):
    if s is None:
        with open('day_09_input.txt', 'r') as f:
            lines = f.read().split('\n')
    else:
        lines = s.split('\n')

    nums = [int(n) for n in lines]
    return nums


def allowed(lst, block=25, prev=None):
    if prev is None:
        acc = []
        for i in range(block-1):
            acc.append([lst[i] + lst[j] for j in range(i+1, block)])
    else:
        raise ValueError('not implemented')
        # acc = prev[1:]
        # for i in range(block-2):
        #     acc[i] = acc[i][1:] + [lst[i] + lst[j] for j in range(block-i+1, block)]
    return acc


def check_allowed(x, allowed):
    ok = any(x in l for l in allowed)
    return ok


def part_01(lst, block=25):
    n = len(lst)
    for i in range(0, n-block):
        ok = check_allowed(
            lst[i+block],
            allowed(lst[i:(block+i)], block=block))
        if not ok:
            return lst[i+block]


def part_01_test():
    s = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
    return s


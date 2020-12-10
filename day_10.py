import numpy as np
import pandas as pd


def read(s=None):
    if s is None:
        with open('day_10_input.txt', 'r') as f:
            lines = f.read().split()
    else:
        lines = s.split()

    nums = list(reversed(sorted([int(n) for n in lines])))
    nums = [max(nums) + 3] + nums
    nums.append(0)
    return np.array(nums)


def part_01_test():
    return """16 10 15 5 1 11 7 19 6 12 4"""


def part_01(lst):
    steps = -(lst[1:] - lst[:-1])
    return sum(steps == 1) * sum(steps == 3)


def part_02(lst):
    # Number of choices from each number
    choices_from = np.array([
        np.sum(((lst[k] - lst) < 4) & ((lst[k] - lst) > 0))
               for k in range(len(lst))
    ])
    choices_to = np.array([
        np.sum(((lst - lst[k]) < 4) & ((lst - lst[k]) > 0))
               for k in range(len(lst))
    ])

    return choices_to, choices_from


def part_01_test_2():
    return """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
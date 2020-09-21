
"""
Author: Akshit Agarwal
Date: 09/20/2020
Link: https://adventofcode.com/2018/day/2
Social: https://www.linkedin.com/in/akshit-agarwal93/
"""


def get_data(fpath):
    with open(fpath, 'r') as f:
        inp = f.read()
    f.close()
    return inp


def part1(s):
    from collections import Counter
    from datetime import datetime
    t0 = datetime.now()
    lines = s.splitlines()
    twos = 0
    threes = 0
    for line in lines:
        # print(line)
        dc = dict(Counter(line))
        cleaned_dc = {}
        for key, value in dc.items():
            if value in [2, 3]:
                cleaned_dc[key] = value
        vals = (list(cleaned_dc.values()))
        # print(vals)
        if (2 in vals) & (3 in vals):
            twos += 1
            threes += 1
        elif 2 in vals:
            twos += 1
        elif 3 in vals:
            threes += 1
    t1 = datetime.now()
    t = (t1 - t0).microseconds
    print(t)

    # print(twos)
    # print(threes)
    print(f'Part 1 answer, twos * threes = {twos * threes}')  # 6642 # 2987μs  #2.987ms


def part2(s):
    from itertools import combinations
    from datetime import datetime
    t0 = datetime.now()
    lines = s.splitlines()
    combs = list(combinations(lines, 2))
    n_chars = len(combs[1][0])
    diss_list = []
    for x, y in combs:
        diss = 0
        for i in range(0, n_chars):
            if x[i] != y[i]:
                diss += 1
        diss_list.append(diss)

    min_diss = min(diss_list)
    idx = diss_list.index(min_diss)
    x, y = combs[idx]
    blank_str = []
    for i in range(0, n_chars):
        if x[i] == y[i]:
            blank_str.append(x[i])
    final_str = "".join(blank_str)
    print(f'Part 2 answer is: {final_str}')  # cvqlbidheyujgtrswxmckqnap #171759μs #172ms
    t1 = datetime.now()
    t = (t1 - t0).microseconds
    print(t)


def main():
    fpath = r'U:\advent of code\day2.txt'
    inp = get_data(fpath)
    part1(inp)
    part2(inp)
    print('test')


if __name__ == '__main__':
    main()

"""
Author: Akshit Agarwal
Date: 09/16/2020
Link: https://adventofcode.com/2018/day/1
Social: https://www.linkedin.com/in/akshit-agarwal93/
"""


def get_data(fpath):
    with open(fpath, 'r') as f:
        inp = f.read()
    f.close()
    return inp


def part1(s):
    lines = s.splitlines()
    val = 0
    for line in lines:
        val += int(line)
    print(f'Part 1 answer is {val}')  # 500


def part2(s):
    lines = s.splitlines()
    val = 0
    seen = {val}
    while True:
        for line in lines:
            val += int(line)
            if val in seen:
                print(f'Part 2 answer is {val}') #709
                return val
            else:
                seen.add(val)


def main():
    fpath = r'U:\advent of code\day1.txt'
    inp = get_data(fpath)
    part1(inp)
    part2(inp)
    print('test')


if __name__ == '__main__':
    main()

def get_data(fpath):
    with open(fpath, 'r') as f:
        inp = f.read()
    f.close()
    return inp


def part1(s):
    # s = 'aA'

    # s = s[:20]
    print(s)
    print(len(s))
    idx = 0
    found = True
    # i
    while found:

        # print(s[idx:idx + 2])
        if not ((idx + 1) <= (len(s) - 1)):
            break
        else:
            try:
                if s[idx].lower() == s[idx + 1].lower():
                    flg = s[idx].islower() != s[idx + 1].islower()
                    if flg:
                        # print(s)
                        rep = s[idx:idx + 2]
                        s = s.replace(rep, '')
                        # print(s)
                        # print('')
                        idx = 0
                idx += 1
            except Exception as e:
                print(f'error at index {idx} in string {s}')
    print(s)
    print(len(s))
    print('test')


def part2(s):
    pass


def main():
    fpath = r'/Users/akshitagarwal/desktop/aoc day5/day5.txt'
    inp = get_data(fpath)
    # part1(inp)
    part2(inp)
    print('complete')


if __name__ == '__main__':
    main()

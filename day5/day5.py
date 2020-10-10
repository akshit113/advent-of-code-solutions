from datetime import datetime


def get_data(fpath):
    with open(fpath, 'r') as f:
        inp = f.read()
    f.close()
    return inp


def part1(s):
    # s = 'dabAcCaCBAcCcaDA'

    # s = s[:20]
    # print(s)
    # print(len(s))
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
                    if flg:
                        # print(s)
                        rep = s[idx:idx + 2]
                        s = s.replace(rep, '')
                        # print(s)
                        # print('')
                        idx = 0
                        continue
                idx += 1
            except Exception as e:
                print(f'error at index {idx} in string {s}')
    # print(s)
    # print(len(s))
    # print('test')
    return s, len(s)


def part2(s):
    # s = 'dabAcCaCBAcCcaDA'
    from numpy import inf
    res = ""
    # for idx in range(97, 97 + 26):
    #     res = res + chr(idx)
    # print(res)

    res = list(set(s.lower()))
    mini = inf
    for i in res:
        new_s = s
        # print(f'removing {i} from {s}')
        new_s = new_s.replace(i, '')
        new_s = new_s.replace(i.upper(), '')
        p1str, st_len = part1(new_s)
        # print(p1str)
        if st_len < mini:
            mini = st_len
            # print(mini)
            poly = p1str
    print(mini)
    # print(p1str)
    print('test')


def main():
    fpath = r'/Users/akshitagarwal/desktop/aoc day5/day5.txt'
    inp = get_data(fpath)
    import time
    start_time = time.time()
    t0 = datetime.now()
    _, _ = part1(inp)
    part2(inp)
    print("--- %s seconds ---" % (time.time() - start_time))
    print('complete')


if __name__ == '__main__':
    main()

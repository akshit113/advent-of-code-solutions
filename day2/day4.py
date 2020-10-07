


def get_data(fpath):
    with open(fpath, 'r') as f:
        inp = f.read()
    f.close()
    return inp


def part1(s):
    from collections import defaultdict, Counter, OrderedDict
    from datetime import datetime
    t0 = datetime.now()

    print(f'\n\nSolving Part 1')
    lines = s.splitlines()
    lines = sorted(lines)

    dc = defaultdict(list)

    i = 0

    s = []
    while i < len(lines):
        istr = lines[i]
        inp = istr.split()

        if 'Guard' in inp:
            id = inp[3]

        if 'falls' in inp:
            ts = inp[0] + " " + inp[1]
            ts = ts[1:len(ts) - 1]
            tm = datetime.strptime(ts, "%Y-%m-%d %H:%M")

        if 'wakes' in istr:
            ts = inp[0] + " " + inp[1]
            ts = ts[1:len(ts) - 1]
            end_time = datetime.strptime(ts, "%Y-%m-%d %H:%M")
            tm_count = int(((end_time - tm).total_seconds()) / 60)
            dc[id].append(tm_count)

        i += 1
    max_sleep = 0
    # print(s)
    for key, value in dc.items():
        s = sum(value)
        if s > max_sleep:
            max_sleep = s
            gid = key

    print(gid)
    sleep = []
    wake = []
    i = 0
    while i < len(lines):
        istr = lines[i]
        # print(istr)
        if gid in istr:
            id = inp[3]
            sleep.append(lines[i + 1])
            wake.append(lines[i + 2])
        i += 1
    # print("\n".join(sleep))
    # print("\n".join(wake))

    cnt_array = []
    rng = list(range(0, len(sleep)))
    for i in rng:
        # print(i)
        sl = int(sleep[i][15:len(sleep) - 2])
        wk = int(wake[i][15:len(wake) - 2])
        while sl < wk:
            cnt_array.append(sl)
            sl += 1

    dc = Counter(cnt_array)
    new = OrderedDict((dc.items()))
    max_occurence = -999999999
    for key, value in new.items():
        if value > max_occurence:
            max_occurence = value
            minute = key
    print(f'max_occurence: {max_occurence}, minute: {minute}')
    final_answer = int(gid[1:]) * minute
    print(f'final answer is {final_answer}')
    t1 = datetime.now()
    t = int((t1 - t0).microseconds/1000)
    print(f'Execution time: {t}ms')


def part2(s):
    from collections import defaultdict, Counter
    from datetime import datetime

    t0 = datetime.now()
    print('\n\nSolving part 2...')
    lines = s.splitlines()
    lines = sorted(lines)
    # print("\n".join(lines))

    # print('sorted')
    dc = defaultdict(list)
    # print(dc)
    i = 0
    while i < len(lines):
        istr = lines[i]
        # print(istr)
        inp = istr.split()

        if 'Guard' in inp:
            id = inp[3]

        if 'falls' in inp:
            ts = inp[0] + " " + inp[1]
            start_time = int(ts[1:len(ts) - 1][-2:])

        if 'wakes' in istr:
            ts = inp[0] + " " + inp[1]
            end_time = int(ts[1:len(ts) - 1][-2:])

            for val in range(start_time, end_time):
                dc[id].append(val)
        i += 1

    max_t = -9999999999
    for key, value in dc.items():
        ct = Counter(value)
        sted = {k: v for k, v in sorted(ct.items(), key=lambda item: item[1])}

        in_key = list(sted.keys())[-1]  # last key,value of sorted dictionary
        in_value = list(sted.values())[-1]

        # find most frequent minute and guard id
        if in_value > max_t:
            max_t = in_value
            minute = in_key
            gid = int(key[1:])

    final_answer = gid * minute
    print(f'gid:{gid}, minute:{minute}, times:{max_t}')
    print(f'final answer is, gid X minute = {final_answer}')
    t1 = datetime.now()
    t = int((t1 - t0).microseconds / 1000)
    print(f'Execution time: {t}ms')


def main():
    fpath = r'/Users/akshitagarwal/desktop/aoc day4/day4.txt'
    inp = get_data(fpath)
    part1(inp)
    part2(inp)
    print('complete')


if __name__ == '__main__':
    main()

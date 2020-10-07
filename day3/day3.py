import numpy

with open('day3.txt') as f:
    lines = [line for line in f]
fabric_matrix = []

for i in range(1000):
    fabric_cols = []
    for y in range(1000):
        fabric_cols.append(0)
    fabric_matrix.append(fabric_cols)

# Part 1
num_blocked = 0

for x in lines:

    pos_x = int(x[x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int(x[x.index(':') + 1:].split('x')[0])
    len_y = int(x[x.index(':') + 1:].split('x')[1])

    for i in range(len_x):
        for j in range(len_y):
            if fabric_matrix[pos_x + i][pos_y + j] == 0:
                fabric_matrix[pos_x + i][pos_y + j] = 1
            elif fabric_matrix[pos_x + i][pos_y + j] == 1:
                fabric_matrix[pos_x + i][pos_y + j] = 2
                num_blocked += 1

print("Part 1: " + str(num_blocked))  # 115304


# Part 2
for x in lines:
    pos_x = int(x[x.index('@') + 1:x.index(':')].split(',')[0])
    pos_y = int(x[x.index('@') + 1:x.index(':')].split(',')[1])
    len_x = int(x[x.index(':') + 1:].split('x')[0])
    len_y = int(x[x.index(':') + 1:].split('x')[1])

    claimed_once = True

    for i in range(len_x):
        for j in range(len_y):
            # print(fabric_matrix[pos_x + i][pos_y + j])

            if fabric_matrix[pos_x + i][pos_y + j] == 2:
                claimed_once = False

    if claimed_once:
        print("Part 2: " + x[x.index('#'):x.index('@') - 1])  # 275
        break

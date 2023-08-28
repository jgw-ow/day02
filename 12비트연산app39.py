door = 65
op = 1 << 31
for i in range(32):
    if door & (op >> i) > 0:
        print(1, end='')
    else:
        print(0, end='')
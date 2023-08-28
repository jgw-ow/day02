BIT_FOR_BYTE = 0
door = 0

def printdoor(door):
op = 1 << BIT_FOR_BYTE - 1
for i in range(BIT_FOR_BYTE):
    if door & (op >> i) > 0:
        print(1, end='')
    else:
        print(0, end='')
        
        
    """
    1번 도어 번호 0
    2번 도어 번호 1
    8번 도어 번호 7
    """
    
    
    printdoor(door)
    door = door | 1 << (BIT_FOR_BYTE - 1 - 0)
    printdoor(door)
    door |= 1 << (BIT_FOR_BYTE - 1 - 7)
    printdoor(door)
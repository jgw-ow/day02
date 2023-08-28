



nums =[10, 20, 30, 40]
iter_nums = iter(nums) #(*10, 20, 30, 40)
try:
    print(iter_nums.__next__())
    print(iter_nums.__next__())
    print(next(iter_nums))
    print(next(iter_nums))
    print(next(iter_nums))
except:
    print("모든 요소를 읽어 들였습니다.")
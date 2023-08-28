nums =[10, 20, 30, 40]
iter_nums = iter(nums) #(*10, 20, 30, 40)
while True:
    try:
        print(iter_nums.__next__())
    except:
        print("모든 요소를 읽어 들였습니다.")
        break
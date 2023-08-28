import time
cnt = 0


def A():
    B()
    
def B():
    A()
    
   
print("제귀호출 횟수 : ", cnt)
print("프로그램을 종료합니다")
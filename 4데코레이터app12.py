def decorator(func):
    def wrapper(n):
        print("함수 실행 전 코드 작성")
        func(n)
        print("함수 실행 후 코드 작성")
    return wrapper
 
@decorator
def work(num):
    print(num, "를 인자로 호출되었습니다.")

work(10)
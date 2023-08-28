
def decorator(func):
    def wrapper():
        print("함수 실행 전 코드 작성")
        func()
        print("함수 실행 후 코드 작성")
    return wrapper
 
@decorator
def work():
    print("함수가 호출되었습니다.")

work()
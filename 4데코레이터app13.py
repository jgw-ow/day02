def decorator(func):
    def wrapper(*args, **kwargs):
        print("함수 실행 전 코드 작성")
        func(*args, **kwargs)
        print("함수 실행 후 코드 작성")
    return wrapper
 
@decorator
def work(msg):
    print(msg)

work("미원")
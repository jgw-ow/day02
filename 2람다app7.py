def resultprinter(func, num):
    result = func(num)
    print(result)
    
#def pow(x):
#    return x ** x

resultprinter(lambda x: x** x, 3)
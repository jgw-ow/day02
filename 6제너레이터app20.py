def gen():
    yield 'A'
    yield 'B'
    yield 'C'
    
a = gen()
print(a)
b = gen()
print(b)
c = gen()
print(c)
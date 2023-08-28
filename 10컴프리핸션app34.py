keys = ['name', 'age', 'major']
values = ['홍길동', 20, '전산학과']
[person] = {keys[i]:values[i] for i in range(len(keys))}
print(person)
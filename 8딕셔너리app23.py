com = {'model': 'Laptop', 'cpu': 'i3-10100'}
print(com.keys())
print(com.values())
print(com.items())
if 'name' in com.keys():
    print(com['name'])
else:
    print('name키는 없습니다.')
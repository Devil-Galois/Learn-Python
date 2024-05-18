#if
cars=['bmw','audi','subaru','toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
requested='mushroom'
if requested!='ok':
    print("hello")
#数值比较
age=18
print((age>17)and(age<20))
print((age<17)or(age<20))
print(True==1)
print(False==0)
#检查特定值是否在列表中
print('bmw' in cars)
print('tramp' in cars)
print('bmw' not in cars)
print('tramp' not in cars)

#bool
gameactive=True
gameend=False

cars=['bmw','audi','toyota','subaru']
print(sorted(cars))
print(sorted(cars,reverse=True))
cars.reverse()
print(cars)
for car in cars:
    print(car)
    print(f"{car} is well!\n")
print("Thanks!")
for value in range(4):
    print(value)
numbers=list(range(5))
print(numbers)
even=list(range(2,11,2))
print(even)
numbers=list(range(1,11))
squares=[]
for value in numbers:
    square=value**2
    squares.append(square)
print(squares)
squares=[value**2 for value in range(1,11)]  #列表解析  列表名=[表达式  for 控制表达式的值]
#使用一个for循环打印1~20
for value in range(1,21):
    print(value)
#一百万求和
numbers=list(range(1,100_0000+1))
print(max(numbers))
print(min(numbers))
print(sum(numbers))
#立方
numbers=[]
for value in range(1,11):
    numbers.append(value**3)
for number in numbers:
    print(number)
#立方解析
numbers=[number**3 for number in range(1,11)]
print(numbers)


#使用列表的一部分
players=['charles','martina','michael','florence','eli']
print(players[0:3])
print(players[1:4])
print(players[:2])#自动从表头开始
print(players[1:])#终止到表尾
print(players[-2:])#从倒数第二个到末尾
#遍历切片
for name in players[1:4]:
    print(name.title())
#复制列表
my_food=['pizza','falafel','carrot cake']
friend_food=my_food[:]
print(friend_food)
#不可行的一种复制列表
my_food=['pizza','falafel','carrot cake']
friend_food=my_food
my_food.append('cannoli')
friend_food.append('ice cream')
print(my_food)
print(friend_food)
#效果是my_food，friend_food都关联到同一个列表
for item in my_food[0:3]:
    print(item)
for item in my_food[1:4]:
    print(item)
for item in my_food[-3:]:
    print(item)



#元组----不可变列表
#定义元组
dimensions=(200,50)
print(dimensions[0])
print(dimensions[1])

my_t=(3,)
for value in dimensions:
    print(value)
#不可以修改元组元素，但可以给存储元组的变量赋值
dimensions=(1,2,3)
print(dimensions)

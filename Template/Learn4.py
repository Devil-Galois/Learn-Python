#if
age=19
if age>=18:
    print('valid')

if age>18:
    print('valid')
    print('ok!')

#if-else
if age<18:
    print('nono')
else:
    print('ok!')

age=12
if age<4:
    print("cost:$0")
elif age<18:
    print('cost:$25')
else:
    print('cost:$40')
#else可以省略
#测试多个条件
requested_topppins=['mushroom','extra cheese']
if 'mushroom' in requested_topppins:
    print(1)
if 'pepperoni' in requested_topppins:
    print(1)
if 'extra cheese' in requested_topppins:
    print(1)
#for循环对列表处理
for element in requested_topppins:
    print(f"{element} is in the list ")
#列表空
requested_topppins=[]
if requested_topppins:
    print('not empty')
else:
    print('empty')

#多列表
available_toppings=['mushroom','olives','green peppers','pepperoni','pineapple'
                    ,'extra cheese']
requested_toppings=['mushroom','fresh fris','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print("Sorry!Not available!")
print('end')




#exercise1
Users=['admin','john','bob','alpha','beta']
for user in Users:
    if user=='admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print(f"Hello {user},thank you for log in again!")
#exercise2
Users=[]
print(Users)
if not Users:
    print("We need to find some users!")
Users=['admin','john','bob','alpha','beta']
new_Users=['john','admin','tom','marry','jam']
lower_Users=[]
for element in Users:
    lower_Users.append(element.lower)
#不区分大小写
for user in new_Users:
    if user.lower in lower_Users:
        print("Sorry!")
    else:
        print("Success!")

numberlist=[1,2,3,4,5,6,7,8,9]
for i in numberlist:
    if i==1:
        print("1st")
    elif i==2:
        print("2nd")
    elif i==3:
        print("3rd")
    else:
        print(f"{i}th")
age = 3
if age < 5:
    print('no')
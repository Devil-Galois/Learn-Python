cars=['bmw','audi','toyota','subaru']
print(sorted(cars))
print(sorted(cars,reverse=True))
cars.reverse()
print(cars)
for car in cars:
    print(car)
    print(f"{car} is well!\n")

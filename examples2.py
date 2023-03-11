x = 22
if x >= 0 and x <= 20:
    print('True')


print('------------------------')

y = 2
if y == 1 or y == 2 or y == 3:
    print('valid')

print('------------------------')

a = 2
b = 4
if a > b: print('a is greater than b')

print('------------------------')

name = 'Ali'
job = 'Developer'

if name == 'Ali':
    print('Name: Ali')
if job == 'Developer':
    print('Nice')

print('-------------------------')

a = 33
b = 33

if b > a:
    print('b is greater than a')
elif a == b:
    print('a and b are equal')

print('-------------------------')

sex = 'Female'
age = 30

if sex == 'male':
    print('Gender: male')
if age <= 31:
        print('he is a young boy')
elif sex == 'Female':
    print('Gender: female')
if age >= 21:
        print('she is a young girl')

print('--------------------------')

sex = 'Female'
age = 30

if sex == 'male':
    if age <= 31:
        print('he is a young boy')
    elif sex == 'Female':
        print('Gender: female')
if age >= 21:
        print('she is a young girl')

print('----------------------------')

num = -3
if num >= 0:
    if num == 0:
        print('0')
    else:
        print('Positiv number')
else:
    print('Negativ number')

print('----------------------------')

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num)

print('----------------------------')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

print('----------------------------')

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    print(day)

print('----------------------------')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

print('----------------------------')

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    print(day)
    if day == "Monday":
        break


print('----------------------------')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)


print('----------------------------')

days = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
for day in days:
    if day == "Monday":
        continue
    print(day)


print('----------------------------')

numbers = [1, 2, 3, 4, 5]
for x in numbers:
    print(x)
else:
    print("Finally finished")


print('----------------------------')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

print('----------------------------')

i = 0
while i < 6:
    print(i)
    i += 1

print('----------------------------')

i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)


print('----------------------------')


i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

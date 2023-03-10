x = 5
s = 'Mahmod Ahmed'
print(type(x))
print(type(s))


print('---------------------')

# python if else example:

x = 500
if x > 600:
    print('x is bigger than 600')
else:
    print('x is smaller than 600')


print('---------------------')


#python elif example:

x = 100
if x == 200:
    print('x = 200')
elif x == 150:
    print('x = 150')
elif x == 300:
    print('x = 300')
else:
    print('this is the default option')
print('rest of the code')


print('---------------------')

#python nested if example:

x = 100
if x < 200:
    print('x is less than 200')

    if x == 150:
        print('x = 150')
    elif x == 50:
        print('x = 50')
elif x < 50:
    print('x is less than 50')
print('rest of the code')


print('---------------------')

#if with boolean operators

name = "mahmod"
age = 21
if name == "mahmod" and age == 21:
    print("welcome mahmod")

if name == "mahmod" or name == "ahmad":
    print("you are not mahmod")
    

print('---------------------')

#python single if example:

x = 100
if x == 100: print('x = 100')


print('---------------------')

#python single if else example:

x = 5
print('x = 5') if x == 5 else print('x != 5')


print('---------------------')

#python conditions example:

birds = {"parakeet": 1, "parrot": 2}
if "parrot" in birds:
    print('there is a parrot')


print('---------------------')

#python conditions example:

birds = {"parakeet": 1, "parrot": 2}
if "automobile" not in birds:
    print('not found')

    
print('---------------------')

#python conditions example:

x = 5
y = 6
z = 3
if all([x == 5, y == 6, z == 3]):
    print('all are true')

if any([x == 2, y == 8, z == 9]):
    print('not all are true')

    
print('---------------------')

#python conditions example:

a = 1
b = 2
if a == 1 and b == 2:
    print(True)

if a == 0 or b == 2:
    print(True)

if not (a == 1 and b == 3):
    print(True)

if a != 0 and b != 3:
    print(True)

print('---------------------')

#python conditions example:

x = 1
if x in (0,2,4):
    print('match')
else:
    print('not found')

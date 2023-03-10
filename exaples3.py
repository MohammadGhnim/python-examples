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

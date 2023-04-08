
'''
write a program to get a list with the numbers of every word or items. 

'''

names = ['alex', 'anna', 'Lokus', 'phillips']

# 1 ---> [4, 4, 5, 8]

result = []
for n in names:
    result.append(len(n))

print(result)


print('--------------------------------')

'''

write a program to get a list with the names, who has more than 3 letters.


'''

#2 ---> names letter > 3

result = []
for n in names:
    if len(n) > 4:
        result.append(n)  #if we want to get the length we write .append(len(n))


print(result)



print('--------------------------------')


'''

Write a program to add new item in a list, with
sorting according to the number of the letter.

'''

def my_insert(names, new):
    for n in names:
        if len(new) < len(n):
            index = names.index(n)
            names.insert(index, new)
            break
    print(names)

names = ['alex', 'anna', 'Lokus', 'phillips']
my_insert(names, 'tt')

'''
write a program to print a list inside a list.

'''

l =['alex', 'anna', [1, 2, 3, 4], 'Lokus']

for i in l:
    if type(i) == list:
        for n in i:
            print(n)
    else:
        print(i)

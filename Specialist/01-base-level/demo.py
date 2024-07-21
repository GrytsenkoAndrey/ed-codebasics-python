n1 = 2
print('n1:', n1)

# есть тройные кавычки
s = '''Hello, 
world!'''
# но этот способ не используется, а используется вот такой способ
n = 'Hello, \
world!'
#print(n)

#####
#number = input('Press your number:')
#print('Your number:', number)

# use placeholder
name = input('Enter your name:')
age = input('Enter your age:')
print('Your name is %s, your age is %s' % (name, age))
# second variant
result = 'Your name is {}, your age is {}'.format(name, age)
print(result)
# в третьем варианте можно указать порядок
res = 'Your name is {1}, your age is {0}'.format(age, name)
print(res)
formstring = f'Your name is {name}, your age is {age}'
print(formstring)
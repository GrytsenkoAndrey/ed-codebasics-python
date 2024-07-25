#
# фнукции для Don't Repeat Yourself
#

def get_employees():
    return 'Список сотрудников'

#print(get_employees())

def print_seconds_per_day(days = 1):
    h = 24 * days
    m = h * 60
    s = m * 60
    return s

# print(print_seconds_per_day(3))

def area_of_disk(radius):
    pi = 3.14159265359
    return pi * radius ** 2

def area_of_ring(outer, inner):
    return area_of_disk(outer) - area_of_disk(inner)

print(area_of_ring(10, 5))

#####
x = 10 # глобальная переменная
def fn(x):
    global x # теперь мы можем изменить глобальную переменную из функции
    print(x) # локальная переменная
    x = 20
    print(x)

print(x)
fn(0)
print(x)

## из функции нельзя изменить глобальную переменную
## но можно ее посмотреть
## плохо, очень плохо обращаться к глоабльным переменным из функций

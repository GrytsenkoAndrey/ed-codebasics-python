#
# фнукции для Don't Repeat Yourself
#

def get_employees():
    return 'Список сотрудников'

#print(get_employees())

def print_seconds_per_day(days):
    h = 24 * days
    m = h * 60
    s = m * 60
    return s

print(print_seconds_per_day(3))

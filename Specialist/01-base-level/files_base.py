#open('test.txt') # open to read
#open('test.txt', 'w') # open to write

# r+ - read and write mode (file must exist)

# REWRITE WHOLE FILE
# w, w+ - read and write mode (file will be created if it doesn't exist)

# APPEND TO FILE
# a, a+ - read and write mode (file will be created if it doesn't exist)

# x - exclusive creation mode (file must not exist)
# t - text mode (default)
# b - binary mode
# r - read mode
# + - read and write mode

#open('test.txt', 'r', encoding='utf-8')

# f = open('test.txt', 'r', encoding='utf-8')
# print(f.read())
# f.close()

# but it's not convenient to close the file every time

# with open('test.txt', 'r', encoding='utf-8') as f:
#     print(f.read()) # in read we can pass the number of symbols to read

# line by line
with open('test.txt', 'r', encoding='utf-8') as f:
    for line in f:
        print(line, end='')
    # or
    #print(f.readlines()) # одна из задач - это зачитать список файла!
    # or
    #s = f.readline()
    #while s:
    #    print(s, end='')
    #    s = f.readline()


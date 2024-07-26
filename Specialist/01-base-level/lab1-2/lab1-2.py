import read_file
import save_file

l = read_file.read_file()
count = len(l)
save_file.save_file('result.txt', l)
print('# Всего уникальных слов: ', count)
print('===============================')
print('# Cписок уникальных слов:')
for i in l:
    print(i)

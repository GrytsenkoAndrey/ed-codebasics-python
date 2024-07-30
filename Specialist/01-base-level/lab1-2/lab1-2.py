import read_file
import save_file

l = read_file.read_file()
save_file.save_file('result.txt', l)

print('# Всего уникальных слов: ', len(l))
print('===============================')
print('# Cписок уникальных слов:')
for i in l:
    print(i)

import csv

#with open('test.csv', 'r', encoding='utf-8') as f:
with open('test.csv', 'a', encoding='utf-8', newline='\n') as f:
    #reader = csv.reader(f, delimiter=',')
    #for row in reader:
    #    print(row)
    writer = csv.writer(f, delimiter=',')
    writer.writerow(['Peter', 'Parker', '43', '432-33-33'])

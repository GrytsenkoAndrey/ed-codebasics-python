def read_file(name = 'text.txt'):
    with open(name, 'r', encoding='utf-8') as file:
        content = file.readlines()
        contentList = content[0].split()
        for i in range(len(contentList)):
            contentList[i] = contentList[i].lower().strip('.,!?«»-')
        s = set(contentList)
        l = list(s)
        l.sort()
        return l

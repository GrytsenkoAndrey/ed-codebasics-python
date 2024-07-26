def save_file(name = 'result.txt', content=None):
    if content is None:
        content = []
    with open(name, 'w+', encoding='utf-8') as file:
        for i in content:
            file.write(i + '\n')
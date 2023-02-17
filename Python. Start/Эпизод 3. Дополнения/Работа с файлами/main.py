# чтение из файла
f = open('file1.txt', 'r')
print(f.read())
f.close()
# запись в файл
g = open('file2.txt', 'w')
g.write('hello\n')

g.writelines(['Hello\n', 'world\n'])
g.close()

# работа с конструкцией  with
with open('file1.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

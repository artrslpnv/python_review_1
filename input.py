import sys
import classes

a = sys.argv[1]
if a == 1:
    m = int(input())
    n = int(input())
    Graph1 = classes.Graph()
    Graph1.initilization(m, n)
    Graph1.dfs()
    lab = classes.Lab()
    lab.initialization(m, n)
    lab.Lab_constructor(Graph1)
    lab.printing()
    print('do u want to see the solution?')
    answer = input()
    if answer == 'yes':
        lab.finding_path((1, 1), (2 * m - 1, 2 * n - 1))
        lab.printing()
    print("save it?(yes/no)")
    answer = input()
    if answer == 'yes':
        print("Enter name")
        name = input()
        file = open(name, 'w')
        file.write(str(Graph1.size1) + '\n' + str(Graph1.size2))
        for i in lab.labirint:
            file.write('\n')
            for j in i:
                if j == 'p':
                    j = 1
                file.write(str(j))
if a == 2:
    m = int(input())
    n = int(input())
    Graph1 = classes.Graph()
    Graph1.initilization(m, n)
    Graph1.Cruckal()
    lab = classes.Lab()
    lab.initialization(m, n)
    lab.Lab_constructor(Graph1)
    lab.printing()
    print('do u want to see the solution?')
    answer = input()
    if answer == 'yes':
        lab.finding_path((1, 1), (2 * m - 1, 2 * n - 1))
        lab.printing()
    print("save it?(yes/no)")
    answer = input()
    if answer == 'yes':
        print("Enter name")
        name = input()
        file = open(name, 'w')
        file.write(str(Graph1.size1) + '\n' + str(Graph1.size2))
        for i in lab:
            file.write('\n')
            for j in i:
                if j == '.':
                    j = 1
                file.write(str(j))

if a == 3:
    print('enter a file name')
    file = open(input())
    h = int(file.readline())
    w = int(file.readline())
    lab = classes.Lab()
    lab.initialization(h, w)
    for i in range(lab.h):
        s = file.readline()
        if s != '\n':
            j = 0
            for item in s:
                if (item != '\n'):
                    lab.labirint[i][j] = int(item)
                    j += 1
    lab.printing()
    print('do u like to print the solution?')
    answer = input()
    if (answer == 'yes'):
        lab.finding_path((1, 1), (2 * h - 1, 2 * w - 1))
        lab.printing()

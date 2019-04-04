import random
from collections import deque


class Graph:
    V = []
    E = []
    size1 = 0
    size2 = 0

    def initilization(self, n, m):
        self.size1 = n
        self.size2 = m
        for i in range(n):
            for j in range(m):
                self.V.append((i, j))

    def dfs(self):  # обычный дфс (вообще переписан с плюсов, кстати я пытался подключать компилятор плюсов ,
        # но из-за него и накрылось все в прошлый раз
        # вместо рекурсии стек  рекурсии ,так как при больших размерах можно и закопаться в рекурсии и программа может
        # упасть,еще есть функция,возвращающая непощенных соседей клетки поля, можно было написать второй граф, где они
        # все бы добавились как ребра и можно было ходить по ним ,но мне было лень;) и я и так не успевал вовремя
        # этот дфс обходит все вершины в порядке тополгоической сортировки и добавляет ребра ,
        # так что остается одна компонента связности в итоге,ну а засчет visited в графе нет циклов

        visited = set()
        reccursion = deque()
        v = (0, 0)
        visited.add(v)

        def not_visited_connected_vertices(y1, x1):
            nonlocal visited

            y = y1
            x = x1
            list_of_not_visited = []
            if (y + 1, x) in self.V and (y + 1, x) not in visited:
                list_of_not_visited.append((y + 1, x))
            if (y - 1, x) in self.V and (y - 1, x) not in visited:
                list_of_not_visited.append((y - 1, x))
            if (y, x - 1) in self.V and (y, x - 1) not in visited:
                list_of_not_visited.append((y, x - 1))
            if (y, x + 1) in self.V and (y, x + 1) not in visited:
                list_of_not_visited.append((y, x + 1))
            return list_of_not_visited

        while len(visited) < self.size1 * self.size2:
            connected = not_visited_connected_vertices(v[0], v[1])
            if len(connected) > 0:
                reccursion.append(v)
                next_v = random.choice(connected)
                self.E.append((v, next_v))
                v = next_v
                visited.add(next_v)
            else:
                v = reccursion.pop()

    def Cruckal(self):
        # cобственно обычный алгоритм краскала начинается с сортировки ребер
        # по весу и обхода их в пордке сортировки и проверки их на то, что они являются мостом
        # но здесь граф невзвешенный поэтому выбирается просто рандомное ребро
        # и  если оно является мостом  между двумя поддеревьями и эти два поддерева обьединяются, а ребро добавляется к ребрам
        # минимального остовного дерева  собственно графа которым потом инициализируется лабиринт
        # вначале все вершины составляют самостоятельные поддеревья ну и так как они обьединяются удобно хранить
        # их в виде множеств а минимальное остовное дерево как массив этих поддеревьев и ждать пока в этом массиве не останется
        # одно множество соответсвенно являющееся ответом.
        minimal_ostov_tree = []
        for i in range(self.size1):
            for j in range(self.size2):
                minimal_ostov_tree.append({(i, j)})
        E1 = set()
        for i in range(self.size1):
            for j in range(self.size2):
                if (i + 1, j) in self.V and ((i, j), (i + 1, j)) not in E1 and ((i + 1, j), (i, j)) not in E1:
                    E1.add(((i, j), (i + 1, j)))
                if (i - 1, j) in self.V and ((i, j), (i - 1, j)) not in E1 and ((i - 1, j), (i, j)) not in E1:
                    E1.add(((i, j), (i + 1, j)))
                if (i, j + 1) in self.V and ((i, j), (i, j + 1)) not in E1 and ((i, j + 1), (i, j)) not in E1:
                    E1.add(((i, j), (i, j + 1)))
                if (i, j - 1) in self.V and ((i, j), (i, j - 1)) not in E1 and ((i, j - 1), (i, j)) not in E1:
                    E1.add(((i, j), (i, j - 1)))
        E1 = list(E1)
        while len(minimal_ostov_tree) != 1:
            edge = random.choice(E1)
            edge1 = list(edge)
            tree1 = set()
            tree2 = set()
            for i in minimal_ostov_tree:
                if edge1[0] in i:
                    tree1 = i
                if edge1[1] in i:
                    tree2 = i
            if not tree1 == tree2:
                t = tree1.union(tree2)
                minimal_ostov_tree.remove(tree1)
                minimal_ostov_tree.remove(tree2)
                minimal_ostov_tree.append(t)
                self.E.append(edge)
            E1.remove(edge)


class Lab:
    h = 0
    w = 0
    labirint = []

    def initialization(self, h1, w1):
        self.h = 2 * h1 + 1
        self.w = 2 * w1 + 1
        for i in range(2 * h1 + 1):
            self.labirint.append([])
            for j in range(2 * w1 + 1):
                if (i % 2) == 1 and j % 2 == 1:
                    self.labirint[i].append(1)
                else:
                    self.labirint[i].append(0)

    def Lab_constructor(self, Graph1):
        if len(Graph1.E) != 0:
            for i in Graph1.E:
                y = i[0][0] + i[1][0] + 1
                x = i[0][1] + i[1][1] + 1
                self.labirint[y][x] = 1
        self.graph = Graph1

    def printing(self):
        for i in range(self.h):
            print('\n')
            for j in range(self.w):
                if self.labirint[i][j]==1:
                    print('-', end=" ")
                elif self.labirint[i][j]==0:
                    print('#', end=" ")
                else:
                    print(self.labirint[i][j], end= " ")

    def finding_path(self, fromm, to):
        #нахождение кратчайшего пути от одной вершины к другой с помощью бфс(как не странно тоже переписано с плюсов,с
        # небольшой стилизацией под специфику представления лабиринта,запускается бфс от стартовой вершины , причем для
       # каждой вершины в массиве ancsectors ее предок то есть вершины запуском бфса от которой наша вершина была вовлечена
        #в алгоритм  таким образом с помощью этого дойдя бфсом до нужной вершины мы с помощью него быстро сможем восстановить путь
        # которым мы пришли в нее и обозначить его спец символами
        def get_connected_vertices(v):
            y = v[0]
            x = v[1]
            list_of_not_visited = []
            if self.labirint[y + 1][x] == 1 and (y + 1, x) not in visited:
                list_of_not_visited.append((y + 1, x))
            if self.labirint[y - 1][x] == 1 and (y - 1, x) not in visited:
                list_of_not_visited.append((y - 1, x))
            if self.labirint[y][x - 1] == 1 and (y, x - 1) not in visited:
                list_of_not_visited.append((y, x - 1))
            if self.labirint[y][x + 1] == 1 and (y, x + 1) not in visited:
                list_of_not_visited.append((y, x + 1))
            return list_of_not_visited

        q = deque()
        visited = set()
        ancsectors = dict()
        ancsectors[fromm] = -1
        q.append(fromm)
        visited.add(fromm)
        while to not in visited:
            v = q.popleft()
            connected = get_connected_vertices(v)
            for i in connected:
                ancsectors[i] = v
                q.append(i)
                visited.add(i)
        v = to
        while (v != -1):
            self.labirint[v[0]][v[1]] = 'p'
            v = ancsectors[v]

class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.nref = None  # ссылка на следующий узел
        self.pref = None  # Ссылка на предыдущий узел


class Queue:
    """
    Основной класс
    """

    def __init__(self):
        self.start = None  # ссылка на начало очереди
        self.end = None  # ссылка на конец очереди

    def isempty(self):
        if self.start == None:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            return None
        else:
            val = self.start.data
            self.start = self.start.nref
            self.start.pref = None
            return val

    def push(self, val):
        if self.isempty():
            self.start = self.end = Node(val)
        else:
            pushednode = Node(val)
            pushednode.pref = self.end
            self.end.nref = pushednode
            self.end = pushednode

    #def insert(self, n, val):

    def print(self):
        currentnode = self.start

        if self.isempty() == True:
            print("Queue is empty")

        else:
            while (currentnode != None):
                print(currentnode.data)
                currentnode = currentnode.nref
        return

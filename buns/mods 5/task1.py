class Node:
    """
    Вспомогательный класс для узлов списка
    """
    def __init__(self, data):
        self.data = data  # храним информацию
        self.pref = None  # ссылка на предыдущий узел

class Stack:
    """
    Основной класс для стека
    """

    def __init__(self):
        self.end = None  # ссылка на конец стека

    def isempty(self):
        if self.end == None:
            return True
        else:
            return False

    def pop(self):
        if self.isempty():
            return None
        else:
            val = self.end.data
            self.end = self.end.pref
            return val

    def push(self, val):
        if self.end == None:
            self.end = Node(val)

        else:
            newnode = Node(val)
            newnode.pref = self.end
            self.end = newnode

    def print(self):
        currentnode = self.end

        if self.isempty() == True:
            print("Stack is empty")

        else:
            while(currentnode != None):
                print(currentnode.data)
                currentnode = currentnode.pref
        return


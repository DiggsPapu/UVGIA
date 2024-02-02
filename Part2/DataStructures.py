class priority:
    def __init__(self, items, comparator):
        self.items = items
        self.comparator = comparator
    def empty(self):
        return  len(self.items) == 0
    def first(self):
        return  self.items[0]
    def remove_first(self):
        if not self.empty():
            return self.items.pop(0)
        return None
    def insert(self, newElement):
        if not self.empty():
            index = 0
            itemsLength = len(self.items)
            while index<itemsLength and self.comparator(newElement, self.items[index]):
                index+=1
            if index<itemsLength:
                self.items.insert(index, newElement)  
            elif index==len(self.items):
                self.items.append(newElement)
        else:
            self.items.append(newElement)

class lifo:
    def __init__(self, items):
        self.items = items
    def empty(self):
        return  len(self.items) == 0
    def first(self):
        return  self.items[len(self.items)-1]
    def remove_first(self):
        if not self.empty():
            return self.items.pop(len(self.items)-1)
        return None
    def insert(self, newElement):
        self.items.append(newElement)
        
class fifo:
    def __init__(self, items):
        self.items = items
    def empty(self):
        return  len(self.items) == 0
    def first(self):
        return  self.items[0]
    def remove_first(self):
        if not self.empty():
            return self.items.pop(0)
        return None
    def insert(self, newElement):
        self.items.append(newElement)
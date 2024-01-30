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
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

def compare_strings(a, b):
    return (a >= b)
  

pq = priority([], compare_strings)
pq.insert("banana")
pq.insert("cherry")
pq.insert("apple")
print(pq.items) # apple
print(pq.remove_first()) # apple
print(pq.items) # banana

import bisect

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
            while self.comparator(newElement, self.items[index]) and index<len(self.items):
                
                index+=1
                self.items.insert(index, newElement)
        else:
            self.items.append(newElement)

def compare_strings(a, b):
    return (a > b) - (a < b)
  

pq = priority([], compare_strings)
pq.insert("apple")
pq.insert("banana")
pq.insert("cherry")
print(pq.first()) # apple
print(pq.remove_first()) # apple
print(pq.first()) # banana

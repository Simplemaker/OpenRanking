import random
class Ranking:
    def __init__(self, items):
        self.items = items
        self.ids = {}
        for i in range(len(self.items)):
            self.ids[i] = self.items[i]
        
        # self.comparisons[i][j] denotes the number of times i is preferred to j
        self.comparisons = [[0 for _ in range(len(items))] for _ in range(len(items))]
    
    def getNextPair(self):
        idA = random.randrange(len(self.items))
        idB = random.randrange(len(self.items))
        return self.items[idA], self.items[idB]
    
    def processPair(self, first, second, firstBetter):
        idA = self.ids[first]
        idB = self.ids[second]
        if not firstBetter:
            idA, idB = idB, idA
        self.comparisons[idA][idB] += 1
    
    
import random

class Ranking:
    def __init__(self, items):
        self.items = items
        self.ids = {}
        for i in range(len(self.items)):
            self.ids[self.items[i]] = i
        
        # self.comparisons[i][j] denotes the number of times i is preferred to j
        self.comparisons = [[0 for _ in range(len(items))] for _ in range(len(items))]
    
    def getNextPair(self):
        idA = random.randrange(len(self.items))
        idB = random.randrange(len(self.items))
        return self.items[idA], self.items[idB]
    
    def processPair(self, first, second, firstBetter=True):
        if first == second:
            return
        idA = self.ids[first]
        idB = self.ids[second]
        if not firstBetter:
            idA, idB = idB, idA
        self.comparisons[idA][idB] += 1
    
    def getRankings(self):
        logits = self.getLogits()
        info = [(logits[i], i) for i in range(len(logits))]
        info.sort(reverse=True)
        order = []
        for (_, i) in info:
            order.append(self.items[i])
        return order
    
    def getLogits(self):
        NUM_ITERATIONS = 100
        p = [1 for _ in range(len(self.items))]
        for _ in range(NUM_ITERATIONS):
            for i in range(len(p)):
                temp_top = 0
                temp_bot = 0
                for j in range(len(p)):
                    if i != j:
                        temp_top += self.comparisons[i][j]
                        temp_bot += (self.comparisons[i][j] + self.comparisons[j][i]) / (p[i] + p[j])
                p[i] = temp_top / temp_bot
            prod = 1
            for val in p:
                prod *= val
            prod **= (1 / len(p))
            if prod != 0:
                for i in range(len(p)):
                    p[i] /= prod
        return p
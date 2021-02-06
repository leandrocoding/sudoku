from random import shuffle
from collections import defaultdict
from collections.abc import Iterator

class ExactcoverSolver(Iterator):

    def __init__(self, constrs, init=(), random=False):
        
        self.random = random
        self.constrs = constrs

        self.choices = defaultdict(set)
        for i in self.constrs:
            for j in self.constrs[i]:
                self.choices[j].add(i)

        self.unsat = set(self.choices)

        self.solu = []

   
        try:
            for i in init:
                self.select_choice(i)
            self.iter = self.solve()
        except KeyError:
     
            self.iter = iter(())

    def select_choice(self, i):
       
        self.solu.append(i)
        for j in self.constrs[i]:
            self.unsat.remove(j)
            for k in self.choices[j]:
                for l in self.constrs[k]:
                    if l != j:
                        self.choices[l].remove(k)

    def unselect_choice(self, i):
       
        last = self.solu.pop()
        assert i == last
        for j in self.constrs[i]:
            self.unsat.add(j)
            for k in self.choices[j]:
                for l in self.constrs[k]:
                    if l != j:
                        self.choices[l].add(k)



    def solve(self):
        if not self.unsat:
           
            yield list(self.solu)
            return

        best = min(self.unsat, key=lambda j:len(self.choices[j]))
        choices = list(self.choices[best])
        if self.random:
            shuffle(choices)

        for i in choices:
            self.select_choice(i)
            yield from self.solve()
            self.unselect_choice(i)

    def __next__(self):
        return next(self.iter)


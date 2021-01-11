from random import shuffle
from collections import defaultdict
from collections.abc import Iterator


class ExactcoverSolver:
    def __init__(self,constrs, startgrid= [], random= False):
        self.constrs = constrs
        self.random = random
        self.choices = defaultdict(set)

        for i in self.constrs:
            for j in self.constrs[i]:
                self.choices[j].add(i)
        self.unsatisfied = set(self.choices)
        self.solution = []
        try:
            for i in startgrid:
                self.select_choice(i)
            return solve
        except KeyError:
            return False
        

    def solve():
        if not self.unsatisfied:
            return list(self.solution)
        best=min(self.unsatisfied,key=lambda j:len(self.choices[j]))
        choices = list(self.choices[best])
        if self.random:
            shuffle(choices)

        for i in choices:
            self.select_choice(i)
            return self.solve()
            self.unselect_choice(i)

        

    def select_choice(self,i):
        self.solution.append(i)
        for j in self.constraints[i]:
            self.unsatisfied.remove(j)
            for k in self.choices[j]:
                for m in self.constraints[k]:
                    if m != j:
                        self.choices[m].remove(k)
    
    def unselect_choice(self, i):
        last = self.solution.pop()
        assert i == last
        for j in self.constraints[i]:
            self.unsatisfied.add(j)
            for k in self.choices[j]:
                for m in self.constraints[k]:
                    if m != j:
                        self.choices[m].add(k)

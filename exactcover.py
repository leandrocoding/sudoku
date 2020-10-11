from random import shuffle
from collections import defaultdict
from collections.abc import Iterator

class Exactcover(Iterator):
    def __init__(self, constraints, initial=(), random=False):
        self.random = random
        self.constraints = constraints
        # print(constraints)
        self.choices = defaultdict(set)
        for i in self.constraints:
            for j in self.constraints[i]:
                self.choices[j].add(i)

        self.unsatisfied = set(self.choices)
        self.solution = []

        try:
            for i in initial:
                self._choose(i)
            self.iter = self._solve()
        except KeyError:
            self.iter = iter(())

    def __next__(self):
        return next(self.iter)

    def _solve(self):
        if not self.unsatisfied:
            yield list(self.solution)
            return
        best=min(self.unsatisfied,key=lambda j:len(self.choices[j]))
        # print(best)
        choices = list(self.choices[best])
        if self.random:
            shuffle(choices)

        for i in choices:
            self._choose(i)
            yield from self._solve()
            self._unchoose(i)

    def _choose(self,i):
        self.solution.append(i)
        for j in self.constraints[i]:
            self.unsatisfied.remove(j)
            for k in self.choices[j]:
                for m in self.constraints[k]:
                    if m != j:
                        self.choices[m].remove(k)

    def _unchoose(self, i):
        last = self.solution.pop()
        assert i == last
        for j in self.constraints[i]:
            self.unsatisfied.add(j)
            for k in self.choices[j]:
                for m in self.constraints[k]:
                    if m != j:
                        self.choices[m].add(k)

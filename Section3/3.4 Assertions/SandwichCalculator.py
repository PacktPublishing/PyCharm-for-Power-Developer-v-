import numpy
from random import randint


class Calculator:
    def __init__(self, my_cost):
        self.charge = 0
        self.my_cost = my_cost

    def markup(self):
        weights = numpy.random.random((3, 3))
        x = randint(0, 2)
        y = randint(0, 2)
        today_weight = weights[x][y] 
        self.charge = self.my_cost * (today_weight )
        # assert self.charge > self.my_cost
        return round(self.charge, 2)

    def family_discount(self):
        self.charge = self.my_cost
        return round(self.charge, 2)

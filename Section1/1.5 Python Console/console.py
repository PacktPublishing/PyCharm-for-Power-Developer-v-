class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        return a / b

    # Todo: Add subtract option

    # def root(a):
    #   return math.sqrt()


def greetings(name):
    print('Hello ' + name + '!')


def goodbye():
    print('Goodbye!')


myCalculator = Calculator
myCalculator.subtract()


# execfile('console.py')
# exec('console.py')

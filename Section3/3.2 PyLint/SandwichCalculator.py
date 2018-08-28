class Calculator:
    def __init__(self, my_cost):
        self.charge = 0
        self.my_cost = my_cost

    def markup(self):
        self.charge = self.my_cost * 1.5
        return round(self.charge, 2)

    def family_discount(self):
        self.charge = self.my_cost * 0.75
        return round(self.charge, 2)


ham = Calculator(6.50)
turkey = Calculator(4.00)

# Print The Menu
print('Ham Sandwich: $' + str(ham.markup()))
print('Ham Sandwich: $' + str(ham.family_discount()) + ' for friends and family')
print('***')
print('Turkey Sandwich: $' + str(turkey.markup()))
print('Turkey Sandwich: $' + str(ham.family_discount()) + ' for friends and family')

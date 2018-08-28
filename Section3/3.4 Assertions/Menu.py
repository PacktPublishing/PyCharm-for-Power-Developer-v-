from Section3.UnitTests.SandwichCalculator import Calculator


class Menu:
    def __init__(self, items):
        self.items = items

    def print_header(self):
        print("~~~~~~~~~~ Melissa's Sandwiches ~~~~~~~~~~")
        print("___________________________________________________ \n")

    def print_menu(self):
        self.print_header()
        for item in self.items:
            sandwich = item[0]
            cost = item[1]
            temp = Calculator(cost)
            charge = round(temp.markup(), 2)


            print(sandwich + ('_' * (20-len(sandwich))) + str(charge))

# ham = ['HAM', 5.50]
# turkey = ['TURKEY', 4.00]
# roast_beef = ['ROAST BEEF', 6.00]
# veggie = ['Veggie', 3.35]
#
# my = Menu([ham, turkey, roast_beef, veggie])
# my.print_menu()

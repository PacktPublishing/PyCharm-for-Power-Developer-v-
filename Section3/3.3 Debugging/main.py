from Section3.Debugging.SandwichCalculator import Calculator


def menu(items, family_disc=False):
    print("\n ~~~ Melissa's Sandwiches ~~~")

    for item in items:
        cost_calculator = Calculator(item[1])

        if family_disc:
            charge = cost_calculator.family_discount()

        else:
            charge = cost_calculator.markup()

        print(item[0] + '.......................${:0.2f}'.format(charge))


if __name__ == "__main__":
    ham = ['HAM', 5.50]
    turkey = ['TURKEY', 4.00]
    roast_beef = ['ROAST BEEF', 6.00]
    veggie = ['Veggie', 3.35]

    menu([ham, turkey, roast_beef, veggie])

from Section3.UnitTests.Menu import Menu


if __name__ == "__main__":
    ham = ['HAM', 5.50]
    turkey = ['TURKEY', 4.00]
    roast_beef = ['ROAST BEEF', 6.00]
    veggie = ['Veggie', 3.35]

    my_menu = Menu([ham, turkey, roast_beef, veggie])
    my_menu.print_menu()

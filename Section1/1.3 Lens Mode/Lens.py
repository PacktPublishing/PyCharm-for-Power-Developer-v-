def markup(my_cost, mark=0.10):
    factor = 1 + mark
    return my_cost*factor


def discount(cost, coupon=0.10):
    my_cost = markup(cost)
    return cost - (cost * coupon)


# Todo: Add family discount method

print('Set python interpreter to 3.x to see errors')






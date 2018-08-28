import json


def make_item(name, bread, meat, cost, charge):
    return {'name': name,
            'bread': bread,
            'meat': meat,
            'my_cost': cost,
            'my_charge': charge
            }


menu = []
menu.append(make_item('Roasted B', 'white', 'Roast Beef', 5.00, 7.00))
menu.append(make_item('Loaded Veggie', 'wheat', None, 3.00, 5.00))
menu.append(make_item('Hammy Lamby', 'wheat', ['ham', 'lamb'], 8.00, 10.00))

with open('menu.json', 'w') as f:
    data = json.dump(menu, f)

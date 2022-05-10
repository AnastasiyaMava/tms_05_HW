import yaml

with open('order.yaml') as file:
    database = yaml.safe_load(file)

order_ID = database['invoice']
print(order_ID)

address = database['ship-to']
print(address)

print("Cost: ", database['total'])
print("Count of products: ", len(database['product']))
print("")

number = 0
for product in database['product']:
    number += 1
    print('Product number: ', number)
    print("Description: ", product['description'])
    print("Quantity: ", product['quantity'])
    print("Cost for 1 unit:  ", product['price'])
    print("Total cost of product: ", product['price'] * product['quantity'])

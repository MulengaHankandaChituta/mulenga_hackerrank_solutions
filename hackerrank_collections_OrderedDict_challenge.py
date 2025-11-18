from collections import OrderedDict

items = OrderedDict()
n = int(input())

for _ in range(n):
    *name, price = input().split()
    item_name = " ".join(name)
    price = int(price)

    if item_name in items:
        items[item_name] += price
    else:
        items[item_name] = price

for item, net_price in items.items():
    print(item, net_price)

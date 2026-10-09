items = [
    ("apple", "fruit"),
    ("banana", "fruit"),
    ("carrot", "vegetable"),
    ("tomato", "vegetable"),
    ("milk", "dairy")
]
grouped_items = dict()

for product, category in items:
    if category in grouped_items:
        grouped_items[category].append(product)
    else:
        grouped_items[category] = [product]

print(grouped_items)

list1 = [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]
list2 = [{"id": 2, "name": "Bob"}, {"id": 3, "name": "Charlie"}]

intersection = []
unique_in_list1 = []
unique_in_list2 = []

for item in list1:
    if item in list2 and item not in intersection:
        intersection.append(item)

for item in list1:
    if item not in list2 and item not in unique_in_list1:
        unique_in_list1.append(item)

for item in list2:
    if item not in list1 and item not in unique_in_list2:
        unique_in_list2.append(item)

print("Пересечение элементов")
print(intersection)
print("Уникальные элементы для первого списка")
print(unique_in_list1)
print("Уникальные элементы для второго списка")
print(unique_in_list2)

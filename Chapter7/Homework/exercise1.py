"""
list1 = [5, 8, 2, 1, 9, 3, 6, 7]
max_number = list1[0]
for i in range(1, len(list1)):
    if list1[i] > max_number:
        max_number = list1[i]

print(list1.index(max_number))
"""
def index_max(formal_list):
    max_number = formal_list[0]
    for i in range(1, len(formal_list)):
        if formal_list[i] > max_number:
            max_number = formal_list[i]
    return formal_list.index(max_number)



list1 = [5, 8, 2, 1, 9, 3, 6, 7]
print(index_max(list1))
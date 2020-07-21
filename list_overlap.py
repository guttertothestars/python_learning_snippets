list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
overlapping_list = []

for number in list1:
    if number in list2:
        overlapping_list.append(number)

revised_overlapping_list = set(overlapping_list)
print(revised_overlapping_list)
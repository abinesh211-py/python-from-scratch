list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = []  # Empty list to store merged elements

i, j = 0, 0  # Pointers for both lists

# Compare elements from both lists and add the smaller one
while i < len(list1) and j < len(list2):
    if list1[i] < list2[j]:
        merged_list.append(list1[i])
        i += 1
    else:
        merged_list.append(list2[j])
        j += 1

# Add remaining elements from list1 (if any)
while i < len(list1):
    merged_list.append(list1[i])
    i += 1

# Add remaining elements from list2 (if any)
while j < len(list2):
    merged_list.append(list2[j])
    j += 1

print("Merged Sorted List:", merged_list)

# Ascending order
def bubble_sort(a_list): # Time complexity: O(n^2) Avg & Worst case, O(n) Best case
    for i in a_list: # Handles the amount of passes required to complete sort
        for j in range(len(a_list) - 1): # Iterates from first element to second to last element
            if a_list[j] > a_list[j + 1]: # Compares current element to next
                # Swapping elements if unordered
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
    return a_list

list1 = [5, 4, 3, 2, 1, 4, 3, 6, 7]
list2 = []
print(bubble_sort(list1))

# User input interface
menu = True
while menu:
    val = input('Input the numbers of your list and when complete input "y" > ')
    if val == 'y':
        menu = False
        print('Your sorted list:')
        print(bubble_sort(list2))
    else:
        list2.append(int(val))
        print(list2)
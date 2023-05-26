# Ascending order
def insertion_sort(a_list): # Time Complexity: O(n^2) Avg & Worst case, O(n) Best case
    for i in range(1, len(a_list)): # Traverse through array from 2nd element (index[1]) to end
        key = a_list[i] # Hold current element in key variable
        j = i-1 # Holds index of previous element in j variable
        # While index is in range and current element is smaller than previous element
        while j >=0 and key < a_list[j]:
            a_list[j + 1] = a_list[j] # Shifts element one position ahead
            j -=1 # Decreases the index to check each previous element
        a_list[j + 1] = key # Shifts the original element to the correct sorted postion
    return a_list

list1 = [5, 4, 3, 2, 1, 4, 3, 6, 7]
list2 = []
print(insertion_sort(list1))

# User input interface
menu = True
while menu:
    val = input('Input the numbers of your list and when complete input "y" > ')
    if val == 'y':
        menu = False
        print('Your sorted list:')
        print(insertion_sort(list2))
    else:
        list2.append(int(val))
        print(list2)
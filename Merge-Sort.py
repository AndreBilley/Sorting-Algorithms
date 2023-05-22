# Ascending order
def merge_sort(a_list):
    if len(a_list) > 1:
        # Find midpoint of list
        midpoint = len(a_list) // 2
        # Create new sublists
        left_list = a_list[:midpoint]
        right_list = a_list[midpoint:]
        # Merge sorting the sublists
        merge_sort(left_list)
        merge_sort(right_list)
        # Sorting variables
        i = j = k = 0 # (i = index of element in left list) (j = index of element in right list) (k = index of element in main list)
        while i < len(left_list) and j < len(right_list): # Loops until every element in the sublists are visited
            # Compares both lists and appends smallest value
            if left_list[i] <= right_list[j]:
                a_list[k] = left_list[i]
                i +=1
            else:
                a_list[k] = right_list[j]
                j +=1
            k +=1
        # Checking for remaining elements in sublists
        while i < len(left_list):
            a_list[k] = left_list[i]
            i +=1
            k +=1
        while j < len(right_list):
            a_list[k] = right_list[j]
            j +=1
            k +=1
        return a_list
    
list1 = [5, 4, 3, 2, 1, 4, 3, 6, 7]
list2 = []    
print(merge_sort(list1))

# User input interface
menu = True
while menu:
    val = input('Input the numbers of your list and when complete input "y" > ')
    if val == 'y':
        menu = False
        print('Your sorted list:')
        print(merge_sort(list2))
    else:
        list2.append(int(val))
        print(list2)

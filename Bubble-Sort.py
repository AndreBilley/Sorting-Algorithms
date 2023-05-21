def bubble_sort(a_list):
    for i in a_list:  # [0,1,2,3,4,5] passes - 5 times
        for j in range(len(a_list) - 1):  # [0,1,2,3,4] passes - 4 times
            if a_list[j] > a_list[j + 1]:
                temp = a_list[j]
                a_list[j] = a_list[j + 1]
                a_list[j + 1] = temp
                # bubble sort is done 'in place' (no extra spaces needed)
    return a_list

list1 = [5, 4, 3, 2, 1, 4, 3, 6 ,7]
print(bubble_sort(list1))
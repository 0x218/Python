#!/usr/bin/python

# Bubble/Sinking sort compares adjacent elements and swaps them if they are in the wrong order.
# The pass through the list is repeated until the list is sorted. 

def bubble_sort(data_list):
    length = len(data_list)
    
    for i in range (length - 1):
        sortRequired = False

        for j in range (length - i - 1): 
            if data_list[j] > data_list[j + 1]: #last 2 pivots
                sortRequired = True
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]
        
        if not sortRequired:
            break
    return data_list


if __name__ == "__main__":
    user_input = input("Enter number separated by comma :")
    unsorted_numbers = [int(num) for num in user_input.split(',')]
    print(bubble_sort(unsorted_numbers))

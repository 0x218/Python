#!/usr/bin/python


# Selection sort is noted for its simplicity.  O(n2) time complexity,  Inefficient on large lists.  
# Performs worse than the similar insertion sort. 

def selection_sort(data_list):
    length  = len(data_list)
    
    for i in range (length - 1):
        leastNum = i #storing index position of least number
        
        for j in range (i+1, length):
            if (data_list[leastNum] > data_list[j]):
                leastNum = j #update index position of least number
        
        if leastNum != i:
            data_list[i], data_list [leastNum] = data_list[leastNum], data_list[i] ##moving least to pivot
    return data_list



if __name__ == "__main__":
    user_input = input("Enter numbers, separate with comma ")
    unsorted_numbers = [int(num) for num in user_input.split(',')]
    print(selection_sort(unsorted_numbers))
import random
import time


def find_min_place(the_list):
    return the_list.index(min(the_list))


def find_two_mins(the_list):
    # find the minimum value in the list, store it in min1_value
    min1_value = min(the_list)
    # find the index of this value, store it in min1
    min1 = the_list.index(min1_value)
    # remove the value from the list
    the_list.remove(min1_value)
    # find the minimum value in the current list
    # find index of this value, store it in min2
    min2 = the_list.index(min(the_list))
    # if needed add 1 to min2
    if min2 >= min1:
        min2 += 1
    # insert back min1_value in the min1's place in the list
    the_list.insert(min1, min1_value)
    # return min1 and min2
    return min1, min2


def find_2_mins(the_list):
    # initialize min1, min1_idx to the lower of the first two elements, min2, min2_idx to the other of the first two elements.
    if the_list[0] <= the_list[1]:
        min1 = the_list[0]
        min1_idx = 0
        min2 = the_list[1]
        min2_idx = 1
    else:
        min2 = the_list[0]
        min2_idx = 0
        min1 = the_list[1]
        min1_idx = 1

    # go through all elements in the list starting at the third one
    # in each place in the list
    #   if the value is lower than min1:
    #       insert min1 & min1_idx into min2 & min2_idx
    #       insert the place & value in min1 & min1_idx
    #   else if it is lower than min2
    #       insert the place & value in min2, min2_idx
    for i in range(2, len(the_list)):
        if the_list[i] < min2:
            if the_list[i] < min1:
                min2 = min1
                min2_idx = min1_idx
                min1 = the_list[i]
                min1_idx = i
            else:
                min2 = the_list[i]
                min2_idx = i

    # return (min1_idx, min2_idx)
    return min1_idx, min2_idx


def make_list(length, max_val):
    the_list = []
    for i in range(length):
        the_list.append(random.randrange(max_val))
    return the_list


def call_func_on_list(func, a_list):
    return func(a_list)


if __name__ == "__main__":
    a_list = make_list(1000000, 1000)
    t1 = time.perf_counter()
    min1, min2 = call_func_on_list(find_two_mins, a_list)
    t2 = time.perf_counter()
    print(min1, min2, 'time:', t2 - t1)
    t1 = time.perf_counter()
    min1, min2 = call_func_on_list(find_2_mins, a_list)
    t2 = time.perf_counter()
    print(min1, min2, 'time:', t2 - t1)

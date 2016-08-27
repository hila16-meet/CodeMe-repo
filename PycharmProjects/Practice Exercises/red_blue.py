"""

1. start_point = index 0
2. blue_idx <- the first blue after start_point
3. red_idx <- the first red after blue_idx. If not found - end.
4. swap: list[blue_idx] <- red, list[red_idx] <- blue
5. start_point <- blue_idx + 1
6. go back to step 2

"""
def red_blue_order(a_list):
    find_blue = False
    find_red = False
    k = 0
    i = 0
    while k < len(a_list):
        while find_blue == False:
            if a_list[i] == "blue":
                blue_idx = i
                find_blue = True
                i += 1
        j = blue_idx + 1
        while find_red == False:
            if a_list[j] == "red":
                red_idx = j
                find_red = True
                j += 1
            elif j == len(a_list):
                break
        a_list[blue_idx] = "red"
        a_list[red_idx] = "blue"
        blue_idx = red_idx
        i = blue_idx + 1
        k += 1
    return a_list



red_blue_order(["red", "red", "blue", "red"])

# *After I do a 'swap' I alredy know where is the next blue, so...
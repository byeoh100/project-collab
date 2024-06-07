def linear_search(val, array):
    for i in range(len(array)):
        if array[i] == val:
            return i

def linear_search_global(val, array):
    ret_array = []
    for i in range(len(array)):
        if array[i] == val:
            ret_array.append(i)
    return ret_array
def find_common_elements(A, B, C):
    set_B = set(B)
    set_C = set(C)
    arr = []

    for element in A:
        if element in set_B and element in set_C and element not in arr:
            arr.append(element)
    
    return arr

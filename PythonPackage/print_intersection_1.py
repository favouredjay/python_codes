def print_intersection():
    str_array = ["1,3,4,5,6,7", "2,3,5,6,7,8"]
    zero = str_array[0].split(",")
    one = str_array[1].split(",")
    str_array.clear()
    for i in zero:
        for j in one:
            if i == j:
                str_array.append(i)
    return str_array


print(print_intersection())

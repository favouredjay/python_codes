def print_intersection():
    array = ["1,2,5,6,7", "2,3,4,5,6"]
    zero = array[0].split(",")
    one = array[1].split(",")
    duplicate = []
    for i in zero:
        for j in one:
            if i == j:
                duplicate.append(i)

    return duplicate


print(print_intersection())
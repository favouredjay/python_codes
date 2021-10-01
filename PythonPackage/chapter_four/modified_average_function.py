def modified_average_function(value, *args):
    average = (value + sum(args) / (value + len(args)))
    return average


print(modified_average_function(1, 2, 2))

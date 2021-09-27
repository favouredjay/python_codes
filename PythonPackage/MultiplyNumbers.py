old_list = [9, 2, 3, 5, 2]
new_list = []


def multiply_numbers(product):
    global j

    for i in len(old_list):
        for j in len(old_list):
            if j == i:
                continue
        product = product * old_list[j]
    new_list.append(product)

    print(product)


multiply_numbers(1)

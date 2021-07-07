values = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 7, 8, 8, 7, 6]


def no_duplicate(duplist):
    no_duplist = []

    for i in duplist:
        if i not in no_duplist:
            no_duplist.append(i)

    return no_duplist


print("The new list size is ", len(no_duplicate(values)))

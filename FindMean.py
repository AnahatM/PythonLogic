def find_mean(set):

    i = 0

    for x in set:
        i += x

    i = i/len(set)

    return i

print(find_mean([1,2,3,5,7,11,13,17,19]))
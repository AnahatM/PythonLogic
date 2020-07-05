#  MAD Calculator.py

"""
MAD:
> Find mean of data set
> Find absolute difference with all terms
> Find the average of absolute differences

"""

data_set = [5,5,3,3,1]

# FIND ABSOLUTE VALUE
def abs(n):
    if n < 0:
        return n * -1
    elif n >= 0:
        return n

# FUNCTION TO FIND THE MEAN
def mean(set):
    i = 0

    for x in set:
        i += x

    i = i/(len(set))
    return i

# FIND THE MEAN
print(f'The mean is {mean(data_set)}')

# TAKE ABSOLUTE DIFFERENCE FROM ALL ITEMS IN LIST
differences = []

for i in data_set:
    i = abs(i-(mean(data_set)))

    differences.append(i)

# GET THE MEAN OF THE DIFERENCES SET
print(f'The M.A.D. is {mean(differences)}')










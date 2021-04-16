from functools import reduce
# TASK 2
def findgreater():
    list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    result = [el[1] for el in enumerate(list) if el[1] > list[el[0] - 1] and el[0] > 0]
    return result


# TASK 3
def divided2120():
    result = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    return result


# TASK 4
def norepeat():
    list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    result = [el for el in list if list.count(el) < 2]
    return result


# TASK 5
def reducer_func(el, prev_el):
    return el * prev_el


def product():
    list = [el for el in range(100, 1001) if el % 2 == 0]
    return reduce(reducer_func, list)

#TASK 6
#A
from itertools import count
def counter(a):
    for el in count(a):
        if el > a + 50:
            break
        else:
            print(el)
#counter(1)

#B
from itertools import cycle
def loop(list):
    b = 0
    for el in cycle(list):
        b += 1
        if(b >= len(list) * 3 + 1):
            break
        print(el)

#loop([1,2,3,4])

#TASK 7
def fact(n):
    for i in range(1, n + 1):
        yield reduce(reducer_func, range(1, i + 1))

#
# for el in fact(5):
#     print(el)

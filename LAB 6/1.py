from functools import reduce
def multy(lis):
    result = reduce(lambda x,y: x*y, lis)
    return result



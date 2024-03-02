def count(string):
    up = sum(1 for i in string if i.isupper())
    low = sum(1 for i in string if i.islower())
    return up, low
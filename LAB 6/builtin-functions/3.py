def polindrom(string):
    return string == ''.join(reversed(string))
print(polindrom('hh'))
def lines(path):
    with open(path, 'r') as file:
        lines = file.readlines()
        return len(lines)

file = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\4.py'
line = lines(file)
print(line)

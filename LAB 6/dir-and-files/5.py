def write(path, data):
    with open(path, 'w') as file:
        for item in data:
            file.write(str(item) + '\n')

file = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\5a.py'
data = [23,24]
write(file, data)

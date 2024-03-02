import os

def dir_and_files(path):
    for item in os.listdir(path):
        if os.path.isdir(os.path.join(path, item)) or os.path.isfile(os.path.join(path, item)):
            print(item)
path = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files'
dir_and_files(path)
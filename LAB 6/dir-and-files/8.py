import os

def delete(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
        else:
            print(f"No write access to {path}. Cannot delete.")
    else:
        print(f"The file {path} does not exist.")


file = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\text files\Y.txt'
delete(file)

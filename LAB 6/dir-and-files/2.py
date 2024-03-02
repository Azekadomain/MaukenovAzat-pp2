import os

def check_path_access(path):
    exists = os.path.exists(path)
    readable = os.access(path, os.R_OK)
    writable = os.access(path, os.W_OK)
    executable = os.access(path, os.X_OK)

    print(f"Exists: {exists}")
    print(f"Readable: {readable}")
    print(f"Writable: {writable}")
    print(f"Executable: {executable}")

path = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files'
check_path_access(path)
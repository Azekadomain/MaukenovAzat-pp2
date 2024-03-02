import os

def analyze_path(path):
    if os.path.exists(path):
        print(f"Path: {path}")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print(f"Directory: {dirname}")
        print(f"Filename: {filename}")
    else:
        print(f"The path {path} does not exist.")

path = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files/3.py'
analyze_path(path)

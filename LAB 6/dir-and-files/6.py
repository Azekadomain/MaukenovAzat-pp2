import string
import os

def generate_text_files(path):
    for letter in string.ascii_uppercase:
        file_name = os.path.join(path, f'{letter}.txt')
        with open(file_name, 'w') as file:
            file.write(f"File {letter}.txt")
dir = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\text files'
generate_text_files(dir)

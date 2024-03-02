def copy(source, dest):
    with open(source, 'r') as source, open(dest, 'w') as dest:
        dest.write(source.read())

source = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\text files\A.txt'
dest = r'C:\Users\a_maukenov\Desktop\LAB 6\dir-and-files\text files\B.txt'
copy(source, dest)

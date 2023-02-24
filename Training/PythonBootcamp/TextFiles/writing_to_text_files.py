with open('myfile.txt', 'w') as f:
    f.write('Just a line\nJust a second line')
    # f.write('Just a second line')

with open('myfile.txt', 'a') as f:
    f.write('Some text here.\n')
    f.write('another text.')

with open('myfile.txt', 'r+') as f:
    f.seek(5)
    f.write('100')
    f.write('Line added with r+\n')
    f.seek(10)
    print(f.read())
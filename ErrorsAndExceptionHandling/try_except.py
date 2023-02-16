f = open('a.txt', 'w')
try:
    f.write('Write something')
except:
    print('Cannot write to file')
else:
    print('File was written successfully')
finally:
    print('This code is always executed')
    if not f.closed:
        f.close()
    print(f'File closed: {f.closed}')

print('some other code')
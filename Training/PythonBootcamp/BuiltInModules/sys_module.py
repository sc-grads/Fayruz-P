import sys
# print(f'Number of arguments: {len(sys.argv)}')
# print(f'This is name of the script:{sys.argv[0]}')
# print(f'The script arguments are: {sys.argv}')

if len(sys.argv) >= 2:
    for item in sys.argv[1:]:
        with open(item, 'r') as f:
            print(f.read())
else:
    print('Wrong no. of arguments')

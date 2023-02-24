import os
os.chdir('insert directory')
i = 1
for file in os.listdir():
    file_name, file_extension = os.path.splitext(file_name)
    # print(file_name, file_extension)

    new_name = f'{str(i)} - song- {file_name}'
    i += 1
    # print(new_name)

    print(f'Renaming {file} to {new_name}')
    os.rename(file, new_name)
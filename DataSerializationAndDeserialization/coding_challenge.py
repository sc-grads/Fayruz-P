# Coding Challenge
#
# In order to simply the serialization and deserialization process your task is:
#
# 1. Create a function called serialize() that takes 3 arguments: 1) the Python object you want to serialize,
# 2) the file to which it serializes the object and 3) the serialization protocol which is pickle or json.
#
# The function will create the file (the 2nd argument) and will write the Python object to that file according to its
# 3rd argument. If the 3rd argument is pickle, It will use pickle to serialize the object and if the argument is json
# it will use json for serialization.
#

def serialize(obj, file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'wb') as f:
            pickle.dump(obj, f)
    elif type == 'json':
        import json
        with open(file, 'w') as f:
            json.dump(obj, f)
    else:
        print('Invalid serialization. Use pickle or json!')


# 2. Create a function called deserialize() that takes 2 arguments: 1) the file which contains serialized data and 2)
# the type of deserialization which is pickle or json.
#
# The function will deserialize from the file into a Python object and will return that object.

def deserialize(file, type):
    if type == 'pickle':
        import pickle
        with open(file, 'rb') as f:
            a = pickle.loads(f)
    elif type == 'json':
        import json
        with open(file, 'rb') as f:
            a = json.loads(f)
    else:
        print('Invalid serialization. Use pickle or json!')
# 3. Test the functions by serializing and deserializing Python objects using both pickle and json.
#
# Note: The script can also be used as a module that will be imported in other Python scripts.

import json
import requests

response = requests.get('https://jsonplaceholder.typicode.com/todos')

todos = json.loads(response.text)

print(type(todos))
print(todos)

for task in todos:
    if task['completed'] == True:
        print(task)
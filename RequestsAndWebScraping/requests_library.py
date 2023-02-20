#################################
## Working with requests
## requests module implements the HTTP prococol
#################################

## Importing the module
import requests

url = 'https://www.python.org'

## Sending a GET request to the server (www.python.org) and saving the response
response = requests.get(url)

print(type(response))  # => Response Object

# All HTTP response status codes are separated into five classes (or categories)
# There are five values for the first digit:
# 1xx (Informational): The request     was received, continuing process
# 2xx (Successful): The request was successfully received, understood, and accepted
# 3xx (Redirection): Further   action needs to be taken in order to complete the request
# 4xx (Client Error): The request contains bad syntax or cannot be fulfilled
# 5xx (Server Error): The server failed to fulfill an  apparently valid request

print(response.status_code)  # => 200 (Success)
print(response.ok)  # => True (False if there was an error)

content = response.content  # response content as a bytes object
print(content.decode())  # decoding to string (HTML Source Code)

print(response.encoding)  # => utf-8

## Getting the HTTP Headers
print(response.headers)    
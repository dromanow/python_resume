import requests
import json

# response = requests.get('https://api.github.com/events')
# print(response.status_code == requests.codes.ok)
# print(response.content)
# print(response.headers)

payload = {
    'key1': 'value1',
    'key2': ['v1', 'v2'],
}

headers = {
    'test_header': 'value1',
}
# response = requests.get('http://httpbin.org/get', params=payload)
# response = requests.put('http://httpbin.org/put')
response = requests.post('http://httpbin.org/post',
                         data=payload,
                         headers=headers,
                         files=
{
    'test_file': open('/home/dromanov/Downloads/examples.zip', 'rb'),
    'test_file_1': '/home/dromanov/Downloads/examples.zip'
})
# response = requests.delete('http://httpbin.org/delete')
print(response.status_code)
print(response.text)


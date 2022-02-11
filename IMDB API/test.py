import requests

payload = {'key1': 'value1', 'key2': 'value2'}
x = requests.get('https://api.github.com/events', data=payload)

print(x.text)

# k_twpxc8hi



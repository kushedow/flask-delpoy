import requests
from requests.exceptions import HTTPError

response = requests.get('https://api.github.com')

print(response.content)
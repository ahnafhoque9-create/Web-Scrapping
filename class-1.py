import requests

website_url = "https://www.jidsbd.org/"

response = requests.get(website_url)

print(response)

print(response.status_code)
import requests
from bs4 import BeautifulSoup

##Learn how to use requests
# response = requests.get("https://oxylabs.io/")
# print(response.content)

## REST API using requests
form_data = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get')
print(response.text)


## BeatifulSoup is a webscrapper but cannot send and fetch requests to the server. That is why we use it along side a request app
url = 'https://oxylabs.io/blog'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser') #TODO what are the other available parsers in beautiful soup
blog_links = soup.find_all('script')
for l in blog_links:
    print("this is a link ")
    print(l)


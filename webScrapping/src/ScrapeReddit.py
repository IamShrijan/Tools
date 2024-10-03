import requests
from bs4 import BeautifulSoup

def scrape_reddit_post(url):
    # Send a GET request to the URL
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)
    
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract post title
    title = soup.find('h1', class_='t3_kwhlrj-post-rtjson-content').text
    
    # # Extract post score
    # score = soup.find('div', class_='_1rZYMD_4xY3gRcSS3p8ODO').text[2]
    
    # # Extract post author
    # author = soup.find('a', class_='_2tbHP6ZydRpjI44J3syuqC').text[3]
    
    # # Extract post content
    # content = soup.find('div', class_='_292iotee39Lmt0MkQZ2hPV').text[4]
    
    # Extract comments
    comments = []
    for comment in soup.find_all('div', class_='md text-14'):
        comment_text = comment.find('div', class_='_292iotee39Lmt0MkQZ2hPV').text
        comments.append(comment_text)
    
    return {
        'title': title,
        'score': score,
        'author': author,
        'content': content,
        'comments': comments
    }

# Example usage
url = 'https://www.reddit.com/r/Python/comments/vncw6d/what_is_the_best_library_for_website_scraping/'
post_data = scrape_reddit_post(url)
print(post_data)

#md text-14 - div for all the comments etc. 
#
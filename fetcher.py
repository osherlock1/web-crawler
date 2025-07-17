#Make HTTP requests for a given URL and fetch the needed data

import requests
from bs4 import BeautifulSoup

def fetch_page(url: str) -> tuple[int, str, str]:
    
    response = requests.get(url)
    status_code = response.status_code

    if status_code == 200:
        #If connected, get html content
        html_content = response.text

        soup = BeautifulSoup(html_content, 'html.parser')
        title_tag = soup.title
        if title_tag:
            title_content = title_tag.text
        else:
            title_content = None
        
        return (status_code, html_content, title_content)

    else:
        raise ValueError(f"Failed to retrieve the webpage.  Status Code: {status_code}")
    
    
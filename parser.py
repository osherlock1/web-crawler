from bs4 import BeautifulSoup

def extract_links(html: str, base_url: str) -> list[str]:

    soup = BeautifulSoup(html, 'html.parser')
    links = soup.find_all('a')

    extracted_links = []
    for link in links:
        href = link.get('href')
        if href:
            extracted_links.append(href)
            
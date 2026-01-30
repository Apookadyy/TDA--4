import html
from bs4 import BeautifulSoup




def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")
    return soup.title.text if soup.title else "No title"
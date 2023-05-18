import re

from bs4 import BeautifulSoup
from urllib import request


def parser(url, tag=""):
    html_page = request.urlopen(url)
    html_content = str(html_page.read().decode(encoding='UTF-8', errors='strict'))
    soup = BeautifulSoup(html_content, "html.parser")
    link_node = soup.find_all('a', href=re.compile(r'' + tag))
    content = ""
    for link in link_node:
        file_name = str(link.text)
        content += file_name + "\r\n"
    return content

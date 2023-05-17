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
        content += str(link.text) + "\r\n"
    return content


def parser_urls(urls={"url": "", "page_num": []}, tag=""):
    content = ""
    start_num = urls["page_num"][0]
    end_num = urls["page_num"][1]
    for i in range(start_num, end_num):
        url = urls["url"].format(str(i))
        print(url)
        content += parser(url, tag)
    return content

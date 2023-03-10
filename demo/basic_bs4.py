#!/usr/bin/env python3

import httpx
from bs4 import BeautifulSoup

url: str = "https://docs.python.org/3/library/functions.html"
req = httpx.get(url)
soup = BeautifulSoup(req.content, "html.parser")

# for link in soup.find_all("a"):
#     if "http" in link.get("href"):
#         print(link.text, link.get("href"))

data = soup.find_all("dl", {"class": "function"})

for item in data:
    print(f"{item.find('code').text}:\n{item.find('p').text}\n")

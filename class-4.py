import requests
from bs4 import BeautifulSoup

web_link = "https://news.ycombinator.com/"

response = requests.get(web_link)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

titlelines = soup.find_all("span", class_="titleline")
authors = soup.find_all("a", class_="hnuser")

for titleline, author in zip(titlelines, authors):
    main_title = titleline.a.text
    author_name = author.text

    print(main_title, "--", author_name, "\n")
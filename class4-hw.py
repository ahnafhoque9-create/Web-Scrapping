import requests
from bs4 import BeautifulSoup

website_link = "https://news.ycombinator.com/news"

response = requests.get(website_link)

html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

titlelines = soup.find_all("span", class_="titleline")
authors = soup.find_all("a", class_="hnuser")
comments = soup.find_all("a", string=lambda text: text and ("comment" in text or text == "discuss"))

for titleline, author, comment in zip(titlelines, authors, comments):
    main_title = titleline.a.text
    author_name = author.text
    comment_text = comment.text

    print(main_title, "--", author_name, "--", comment_text, "\n")
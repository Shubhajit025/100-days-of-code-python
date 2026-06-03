from pprint import pprint
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)

    link = article_tag.find(name="a").get("href")
    article_links.append(link)

# print(article_texts)
# print(article_links)
# print(article_upvotes)
# print(int(article_upvotes[0].split()[0]))

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(f"Most Popular article --> {article_texts[largest_index]}")
print(f"Link of the article --> {article_links[largest_index]}")
print(f"Total Upvotes gained --> {article_upvotes[largest_index]}")







# import lxml --> we will use 'lxml' if html.parser not working
# with open("website.html") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.a)
# # print(soup.li)
# # print(soup.p)
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# all_anchor_tags_p = soup.find_all(name="p")
# print(all_anchor_tags_p)
#
# for tags in all_anchor_tags:
#     # print(tags.getText())
#     print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.string)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.string)
#
# company_url = soup.select_one(selector="p a")
# print(company_url.get("href"))
#
# company_name = soup.select_one(selector="#name")
# print(company_name.getText())
#
# company_class = soup.select(selector=".heading")
# print(company_class[1].getText())


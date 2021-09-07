import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable

# response = requests.get("https://www.bbc.com/news")
# soup = BeautifulSoup(response.text, "html.parser")
# title_container = soup.find_all("h3", class_="gs-c-promo-heading__title")
# link_container = soup.find_all("a", class_="gs-c-promo-heading")
#
# titles = []
# links = []
#
# for title in title_container[1:]:
#     titles.append(title.get_text())
#
#
# for link in link_container[:len(titles)]:
#     if link.get("href").startswith("/"):
#         link = "https://www.bbc.com" + link.get("href")
#     else:
#         link = link.get("href")
#     links.append(link)
#
#
# table = PrettyTable()
#
# table.add_column("News Title", titles)
# table.add_column("News Link", links)
#
# print(table)


def get_article():
    bbc_request = requests.get('https://www.bbc.com/news')
    soup = BeautifulSoup(bbc_request.text, "html.parser")
    raw_article = soup.find_all('div', {'class': 'gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'})[0].find_all(text=True, recursive=True)
# Checking if article has video and then moving index by 1 for proper display in message
    if raw_article[0].startswith('Video'):
        topic = raw_article[5]
        title = raw_article[1]
        description = raw_article[2]
        publish_time = raw_article[4]
    else:
        topic = raw_article[4]
        title = raw_article[0]
        description = raw_article[1]
        publish_time = raw_article[3]
    href = soup.find_all('div', {'class': 'gs-c-promo-body gel-1/2@xs gel-1/1@m gs-u-mt@m'})[0].find('a', {'class': 'gs-c-promo-heading gs-o-faux-block-link__overlay-link gel-pica-bold nw-o-link-split__anchor'})['href']
    link = f' https://www.bbc.com{href}'
    article = f'✏️ <b>Topic</b>:  {topic}\n⚠️ <b>Title</b>:  {title}\n📌 <b>Description</b>:  {description}\n🕒 <b>Published</b>:  {publish_time}\n➡️ <b>Full article</b>: {link}'
    return article


print(get_article())

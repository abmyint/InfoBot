import requests
from bs4 import BeautifulSoup
from prettytable import PrettyTable


def get_song():
    response = requests.get(f"https://www.billboard.com/charts/hot-100")
    soup = BeautifulSoup(response.text, 'html.parser')
    titles = [title.get_text() for title in soup.find_all("span", class_="chart-element__information__song")[:10]]
    artists = [artist.get_text() for artist in soup.find_all("span", class_="chart-element__information__artist")[:10]]

    # table = PrettyTable()
    # table.add_column("Rank", [rank for rank in range(1, len(title)+1)])
    # table.add_column("Title", title,)
    # table.add_column("Artist", artist)
    info = ''
    for i, title, artist in zip(range(1, len(titles)+1), titles, artists):
        info += f"<b>{i}</b>    <b>Title</b>:  {title}     <b>🎤Artist</b>:   <i>{artist}</i>\n"
    return info


# print(get_song())

# print(get_song())

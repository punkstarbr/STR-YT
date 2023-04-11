import requests
from bs4 import BeautifulSoup
import datetime
import streamlink
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Arquivo de saída deve ter um nome diferente
m3u8_file = open("lista_vimeo.m3u", "w")

# Aqui você pode mudar o número de páginas a serem extraídas
for i in range(1, 3):
    url = f"https://vimeo.com/search/page:{i}/sort:latest?q=aula"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
    video_links = [item["href"] for item in soup.find_all("a", class_="item")]
    # Variável Data já é uma palavra reservada do Python, renomeie para algo diferente
    video_dates = [item.text for item in soup.find_all("span", class_="item-date")]

    for title, link in zip(video_titles, video_links):
        now = datetime.datetime.now()
        timestamp = now.strftime("%m%d%H%M%S")
        video_url = streamlink.streams(link)["720P"].url if streamlink.streams(link) else None
        item = soup.find("a", class_="item", href=link)
        try:
            image_url = item.find("img")["src"]
        except Exception as e:
            print(f"Error: {e}")
            image_url = "https://i.vimeocdn.com/portrait/74133809_44x44?subrect=88%2C88%2C1792%2C1792&r=cover"
        if video_url:
            m3u8_file.write(f"#EXTINF:-1 group-title=\"VIMEO\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")

time.sleep(15)

# Feche o arquivo ao final do código
m3u8_file.close()

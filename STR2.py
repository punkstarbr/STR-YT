import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp

# Configurando opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_tvi = "https://tviplayer.iol.pt/videos/ultimos"

# Abrir a página desejada
driver.get(url_tvi)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Obter o HTML da página
html = driver.page_source

# Analisar o HTML com o BeautifulSoup para extrair os títulos, links, legendas e imagens dos vídeos
soup = BeautifulSoup(html, "html.parser")
video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
subtitles = [item.text for item in soup.find_all("span", class_="item-program-title")]
images = [item['style'].split('url(')[1].split(')')[0] for item in soup.select("a.item")]

# Loop através dos vídeos para extrair as informações de streaming usando yt_dlp e escrever no arquivo M3U8
with open("lista2str2.m3u", "w") as m3u8_file:
    for title, link, subtitle, image_url in zip(video_titles, video_links, subtitles, images):
        # Obtém informações de streaming com yt_dlp
        with yt_dlp.YoutubeDL({}) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            formats = info_dict.get('formats', None)
        
        # Escreve as informações dos vídeos no arquivo de saída no formato M3U8
        for f in formats:
            if f.get('ext') == 'm3u8':
                m3u8_url = f.get('url')
                m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{subtitle} - {title}\n{m3u8_url}\n")
                m3u8_file.write("\n")
                break

# Fechar o driver do Chrome
driver.quit()

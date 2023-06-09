import requests
from bs4 import BeautifulSoup
import datetime
import streamlink
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Configurando opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da primeira página
url_tvi = "https://tviplayer.iol.pt/videos/ultimos/1/canal:"

# Abre o arquivo de saída em modo de escrita
with open("lista2str2.m3u", "w") as m3u8_file:
    
    # Loop através das páginas para extrair os vídeos
    for i in range(1, 2):
        # URL da página atual
        url_tvi = f"https://tviplayer.iol.pt/videos/ultimos/{i}/canal:"
        
        # Abrir a página atual
        driver.get(url_tvi)
        
        # Aguardar alguns segundos para carregar todo o conteúdo da página
        time.sleep(5)
        
        # Obter o HTML da página atual
        html = driver.page_source
        
        # Analisar o HTML com o BeautifulSoup para extrair os títulos, links, legendas e imagens dos vídeos
        soup = BeautifulSoup(html, "html.parser")
        video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
        video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
        subtitles = [item.text for item in soup.find_all("span", class_="item-program-title")]
        images = [item['style'].split('url(')[1].split(')')[0] for item in soup.select("a.item")]

        # Loop através dos vídeos para extrair as informações de streaming usando Streamlink e escrever no arquivo M3U8
        for title, link, subtitle, image_url in zip(video_titles, video_links, subtitles, images):
            now = datetime.datetime.now()
            timestamp = now.strftime("%m%d%H%M%S")

            # Obtém a URL do vídeo em formato M3U8 com a biblioteca Streamlink
            try:
                streams = streamlink.streams(link)
                if 'best' in streams:
                    video_url = streams['best'].url
                else:
                    video_url = streams[list(streams.keys())[0]].url
            except Exception as e:
                print(f"Erro ao obter a URL do vídeo {title}: {e}")
                video_url = None

            if video_url:
                m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{subtitle} - {title}\n{video_url}\n")
                m3u8_file.write("\n")

    # Fechar o driver do Chrome após o término do loop
    driver.quit()

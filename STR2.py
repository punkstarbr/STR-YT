import requests
from bs4 import BeautifulSoup
import datetime
import streamlink
import time

# Define um cabeçalho HTTP para simular o acesso através de um navegador web
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

# Abre o arquivo de saída em modo de escrita
with open("lista2str2.m3u", "w") as m3u8_file:

    # Percorre as páginas com os vídeos recentes da TVI Player
    for i in range(1, 6):
        url = f"https://tviplayer.iol.pt/videos/ultimos/{i}/canal:"
        
        # Faz uma requisição HTTP para obter o HTML da página
        response = requests.get(url, headers=headers)
        
        # Analisa o HTML com o BeautifulSoup para extrair os títulos, links, legendas e imagens dos vídeos
        soup = BeautifulSoup(response.content, "html.parser")
        video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
        video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
        subtitles = [item.text for item in soup.find_all("span", class_="item-program-title")]
        images = [item['style'].split('url(')[1].split(')')[0] for item in soup.select("a.item")]
        
        # Escreve as informações dos vídeos no arquivo de saída no formato M3U8
        for title, link, subtitle, image_url in zip(video_titles, video_links, subtitles, images):
            now = datetime.datetime.now()
            timestamp = now.strftime("%m%d%H%M%S")
            
            # Obtém a URL do vídeo em formato M3U8 com a biblioteca streamlink
            try:
                video_url = streamlink.streams(link)["best"].url
            except Exception as e:
                print(f"Erro ao obter a URL do vídeo {title}: {e}")
                video_url = None
            
            if video_url:
                m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{subtitle} - {title}\n{video_url}\n")
                m3u8_file.write("\n")
        
        # Aguarda 13 segundos antes de acessar a próxima página de vídeos
        time.sleep(13)
        
    # Fecha o arquivo de saída após o término do loop
    m3u8_file.close()

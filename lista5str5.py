import subprocess
import os

# Instalando yt-dlp
subprocess.run(['sudo', 'wget', 'https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp', '-O', '/usr/local/bin/yt-dlp'])
subprocess.run(['sudo', 'chmod', 'a+rx', '/usr/local/bin/yt-dlp'])

# Instalando youtube-dl
subprocess.run(['sudo', 'wget', 'https://yt-dl.org/downloads/latest/youtube-dl', '-O', '/usr/local/bin/youtube-dl'])
subprocess.run(['sudo', 'chmod', 'a+rx', '/usr/local/bin/youtube-dl'])
subprocess.run(['youtube-dl', '-U'])


# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

# Get LISTA4.m3u8
with open('./LISTAMASTER.m3u', 'w') as f:
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")
    f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
    title = subprocess.run(['yt-dlp', '--get-title', 'https://www.youtube.com/c/GuilhermeMartinsTV/videos'], stdout=subprocess.PIPE)
    title = title.stdout.decode().strip()
    thumbnail = subprocess.run(['yt-dlp', '--get-thumbnail', 'https://www.youtube.com/c/GuilhermeMartinsTV/videos'], stdout=subprocess.PIPE)
    thumbnail = thumbnail.stdout.decode().strip()
    url = subprocess.run(['yt-dlp', '--get-url', 'https://tviplayer.iol.pt/direto/CNN'], stdout=subprocess.PIPE)
    url = url.stdout.decode().strip()
    f.write(f"#EXTINF:-1 tvg-id='{title}' tvg-logo='{thumbnail}',{title}\n")
    f.write(f"{url}\n")

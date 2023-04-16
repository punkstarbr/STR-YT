#! /usr/bin/python3

import requests
import os
import sys
import subprocess
from bs4 import BeautifulSoup
import re

banner1 = r'''
###########################################################################
#                                                                         #
#                                  >> https://github.com/guiworldtv       #
###########################################################################
#EXTM3U
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL 1
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_1080p.m3u8

#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="Argentina",UNIFE TV  25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/98adedd6dec04a2d8663899b927f9383/chunklist_b4628000.m3u8
#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"
'''

banner2 = r'''
#EXTM3U
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal 26 (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://fonts.gstatic.com/s/i/productlogos/lens_camera/v1/192px.svg",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8

https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8
'''

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        if windows:
            print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
            return
        os.system(f'wget {url} -O temp.txt')
        response = ''.join(open('temp.txt').readlines())
        if '.m3u8' not in response:
            print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
            return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://github.com/Nicolas0919/Guia-EPG/raw/master/GuiaEPG.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/directv.com.ar.epg.xml.gz"')

print(banner1)

with open('../ARGENTINA.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
print(banner2)

if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')

# Rest of the code

def search_image_url(channel_name):
    query = f"{channel_name} logo filetype:png OR filetype:jpg"
    search_url = f"https://www.google.com/search?q={query}&tbm=isch"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
    }
    response = requests.get(search_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        img_tags = soup.find_all("img")

        for img_tag in img_tags:
            img_url = img_tag["src"]
            if re.match(r'^https?://', img_url):
                return img_url

    return None

def is_channel_working(url, headers=None):
    try:
        cmd = [
            "ffmpeg",
            "-headers",
            f"User-Agent: {headers['User-Agent']}" if headers and "User-Agent" in headers else "User-Agent: python-requests/2.25.1",
            "-i",
            url,
            "-t",
            "10",
            "-f",
            "null",
            "-"
        ]

        process = subprocess.run(cmd, stderr=subprocess.PIPE, universal_newlines=True, timeout=5)
        return process.returncode == 0
    except (subprocess.TimeoutExpired, subprocess.CalledProcessError):
        return False

repo_urls = [
    "https://github.com/pendy99/iptv-epg/raw/18f59d7c25ff694dbf8c053ed4e069a1cb62d841/iptv_channels_argentina.m3u"
]

working_channels = []

for url in repo_urls:
    m3u_response = requests.get(url)

    if m3u_response.status_code == 200:
        m3u_lines = m3u_response.text.splitlines()

        for i, line in enumerate(m3u_lines):
            if line.startswith("#EXTM3U"):
                working_channels.append({"extm3u_line": line})
            elif line.startswith("#EXTINF"):
                extinf_line = line
                extvlcopt_line = None
                kodiprop_lines = []
                stream_url = None
                headers = {}

                for j in range(i + 1, len(m3u_lines)):
                    next_line = m3u_lines[j]

                    if next_line.startswith("#EXTVLCOPT"):
                        extvlcopt_line = next_line
                        if "http-user-agent" in extvlcopt_line:
                            user_agent = extvlcopt_line.split("=")[1]
                            headers["User-Agent"] = user_agent
                    elif next_line.startswith("#KODIPROP"):
                        kodiprop_lines.append(next_line)
                    elif not next_line.startswith("#"):
                        stream_url = next_line
                        break

                if stream_url:
                    should_add_channel = is_channel_working(stream_url, headers) or stream_url.startswith("https://video-auth") or stream_url.startswith("https://d1zx6l1dn8vaj5.cloudfront.net/out/v1/b89cc37caa6d418eb423cf092a2ef970")
                    if should_add_channel:
                        working_channels.append({
                            "extinf_line": extinf_line,
                            "extvlcopt_line": extvlcopt_line,
                            "kodiprop_lines": kodiprop_lines,
                            "stream_url": stream_url
                        })

# Print the working channels
for channel in working_channels:
    if "extm3u_line" in channel:
        print(f"{channel['extm3u_line']}\n")
    else:
        extinf_line_parts = channel['extinf_line'].split(',', 1)
        channel_info = extinf_line_parts[0].strip()
        channel_name = extinf_line_parts[1].strip()

        # Modificar group-title para "Argentina"
        group_title_pattern = re.compile(r'group-title="[^"]*"')
        if group_title_pattern.search(channel_info):
            channel_info = group_title_pattern.sub('group-title="Argentina"', channel_info)
        else:
            channel_info += ' group-title="Argentina"'

        if "tvg-logo" not in channel_info or 'tvg-logo=""' in channel_info or 'tvg-logo="N/A"' in channel_info:
            image_url = search_image_url(channel_name)
            if image_url:
                if "tvg-logo" not in channel_info:
                    channel_info += f' tvg-logo="{image_url}"'
                else:
                    channel_info = channel_info.replace('tvg-logo=""', f'tvg-logo="{image_url}"')
                    channel_info = channel_info.replace('tvg-logo="N/A"', f'tvg-logo="{image_url}"')

        channel['extinf_line'] = f"{channel_info},{channel_name}"

        print(f"{channel['extinf_line']}\n")
        if channel['extvlcopt_line']:
            print(f"{channel['extvlcopt_line']}\n")
        for kodiprop_line in channel['kodiprop_lines']:
            print(f"{kodiprop_line}\n")
        print(f"{channel['stream_url']}\n")


if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')

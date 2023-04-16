#! /usr/bin/python3

import requests
import os
import sys
import subprocess
from bs4 import BeautifulSoup
import re

banner = r'''
###########################################################################
#                                                                         #
#                                  >> https://github.com/guiworldtv       #
###########################################################################
EXTINF:-1 xui-id="130" tvg-id="TVNSTGO" tvg-name="TVN" tvg-logo="https://normielista.cl:443/images/0GV_IuQaPDLyYaZp9L5H2CMg2ozhFk3H2yn6s37Y4X9hjyeejv4VZTPJ0cqZW1Oo.png" group-title="CHILE",TVN
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9RH4Lwij7wZqoExyEgsq1MJiZehEJxZd2QnpUVeLV_Fz/ts
#EXTINF:-1 xui-id="125" tvg-id="CHVAAH" tvg-name="Chilevisión" tvg-logo="https://normielista.cl:443/images/0GV_IuQaPDLyYaZp9L5H2CMg2ozhFk3H2yn6s37Y4X_0xaKkuCYoGKPL_-hbrOy6TaaN6EC_eDJyzmXiMgM4Gg.png" group-title="CHILE",Chilevisión
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBNaTAhytRXgJHnEzvivdqpz/ts
#EXTINF:-1 xui-id="128" tvg-id="MEGA" tvg-name="Mega" tvg-logo="https://normielista.cl:443/images/0GV_IuQaPDLyYaZp9L5H2CMg2ozhFk3H2yn6s37Y4X-phSNZlGbmiki05OMDvwB3.png" ggroup-title="CHILE",Mega
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBMsnAqGqGPj2vyAPsUBpsmZ/ts

#EXTINF:-1 xui-id="123" tvg-id="C13STGO" tvg-name="Canal 13" tvg-logo="https://normielista.cl:443/images/0GV_IuQaPDLyYaZp9L5H2CMg2ozhFk3H2yn6s37Y4X9UAj6nCi9ytepPsaKrCz8k.png" group-title="CHILE",Canal 13
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBPoLH-GYNntm7KysNxxPI6Z/ts
#EXTINF:-1 xui-id="124" tvg-id="C24HCHD" tvg-name="Canal 24 Horas" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2IPJinOlJVnENfBFlS2f8OG6I2OZk9mzRggeMoyTj1kc6X6UzJnYGZx-2GvwWcigHw.png" group-title="CHILE"Canal 24 Horas
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBM1P5bOvAcCwsZBXSDDyluK/ts
#EXTINF:-1 xui-id="126" tvg-id="CNNCHHD" tvg-name="CNN Chile" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2CQmSialG6ZFMmnpVE7A3yr7cr6gkEqI4oAEDNOhlD8CfS4oWAPnSbp-qLL8lUx_cw.png" group-title="CNN's" group-title="CHILE",CNN Chile
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBPGhQ9E8F4wKThv_TnShSCq/ts


#EXTINF:-1 xui-id="211" tvg-id="TELECAN" tvg-name="Telecanal" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2GwUee_HeV47TzX8gNpnfyD4YmEoqWUnSgobe7GrT8ZD-0ouPKy3e0dcXJRw_Tz3Pw.png" group-title="CHILE",Telecanal
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9aLNkFkv3hiRbFq-IldfOLt_UbOCl9KbIozLEa8E7hGq/ts
#EXTINF:-1 xui-id="127" tvg-id="LARSTGO" tvg-name="La Red" tvg-logo="https://normielista.cl:443/images/0GV_IuQaPDLyYaZp9L5H2CMg2ozhFk3H2yn6s37Y4X-38hpTEMj3jiXZuXV1Wu0n.png" group-title="CHILE",La Red
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBPSYTI7ma7Kq8RdDrV2MVjD/ts
#EXTINF:-1 xui-id="129" tvg-id="TVMAS" tvg-name="TV+" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2GwUee_HeV47TzX8gNpnfyDYJ6p7Kx-jfO4caNakoUhllyFnR5yWYSnRv4lnoRMwPA.png" ggroup-title="CHILE",TV+
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9VTVNpb0Ty6APnEPt0h4YBN-QdWvfzXcmwCqNlLe77eJ/ts

#EXTINF:-1 xui-id="151" tvg-id="TDCLVHD" tvg-name="Discovery Channel" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2CQmSialG6ZFMmnpVE7A3yqON5YO_qN3tthlYeEufoUOqJP914nRtNv6GRAI4Jfu5A.png" ggroup-title="CHILE",Discovery Channel
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9U3VvRIXL7HaW-FbHrzwKyPiuztYG1AN5PMmsGlPN9Ry/ts
#EXTINF:-1 xui-id="180" tvg-id="NGCARGA" tvg-name="National Geographic Channel" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2I7gRHQqlt2urJ_cA-odHswb6x4e_G074Gnl5R6p3lC_zSnMKvu1W2w2Nbp0M8r2YA.png" group-title="CHILE",National Geographic Channel
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9cJ27zzRXaUVifkaTkP6RywvEgUce_3dNBoNeiMKinhX/ts
#EXTINF:-1 xui-id="171" tvg-id="HCCHDA" tvg-name="History Channel" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2PncQnjvX0UIbf-mXiFDYhhRHpsWl0xSTi7hPPFBCAuLQS5yOHjOjCFVYrkZQGabaQ.png" group-title="CHILE",History Channel
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9Z6cf5QAjTDyhklY3sDH2YoSMiZtRs2Xqoh9XnYGyMA0/ts
#EXTINF:-1 xui-id="333" tvg-id="ESFNCHD" tvg-name="Fox News" tvg-logo="https://normielista.cl:443/images/HM3xx55KZnCUdlPuNC1k2PncQnjvX0UIbf-mXiFDYhhOHwSbMMlbnwuAOu1KXpBkJpAPp-cnmoi2v3IoqrzA6A.png" group-title="CHILE",Fox News
https://normielista.cl:443/play/0Bu2UVekNecKvoeYhzqb9UqZX_r3sEm2Oti6aB1NpsGldgY8qBJs1y9ueFjdkDcR/ts

'''

banner2 = r'''
#EXTINF:-1 tvg-logo="https://i.imgur.com/5fEIf7q.png" group-title="Radios Chilenas Con Video",-Radios Chilenas Con Video-
https://i.imgur.com/7o6at8Q.mp4
#EXTINF:-1 tvg-logo="https://i.imgur.com/c2qDoi3.png" group-title="Radios Chilenas Con Video",Chocolate FM | SD | Maipú
https://paneltv.online:1936/8106/8106/chunklist_w1524549576.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/G5UGhwA.png" group-title="Radios Chilenas Con Video",Favorita TV | SD | Curicó
http://streamyes.alsolnet.com/radiofavoritatv/live/chunklist_w2007168887.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/IaTIPLW.png" group-title="Radios Chilenas Con Video",Pulso | SD | Santiago
https://panel.tvstream.cl:1936/8004/8004/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/SkcUAno.png" group-title="Radios Chilenas Con Video",Radio Rancagua TV| SD | Rancagua
https://5d1ca66d2d698.streamlock.net:1936/8056/8056/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/S8VPPgr.png" group-title="Radios Chilenas Con Video",Red Fueguina Medios | SD | Porvenir
https://inliveserver.com:1936/11012/11012/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/Vt424Nn.png" group-title="CHILE",TVN CHILE | FHD | Santiago | Alt.
https://onx.la/0c2f3.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/PrG6SkZ.png" group-title="CHILE",Chilevisión | SD | Santiago | Alt.
https://onx.la/fe0aa.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/ILZeBjW.png" group-title="CHILE",Canal 13 | SD | Santiago | Alt.
https://onx.la/3aa24.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/puJ88Pk.png" group-title="CHILE",La Red | FHD | Santiago 2
https://d2ab26kihxq8p0.cloudfront.net/hls/live.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/27i6iYB.png" group-title="CHILE",UCV2 | HD | Valparaíso
https://unlimited10-cl.dps.live/ucvtveventos/ucvtveventos.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/ilCiqga.png" group-title="CHILE",Canal 21 | HD | Chillan
https://tls-cl.cdnz.cl/canal21tv/live/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/dPUYBfM.png" group-title="CHILE",Bio Bio TV | FHD | Providencia
https://pantera1-100gb-cl-movistar.dps.live/bbtv/bbtv.smil/bbtv/livestream2/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/sL057W6.png" group-title="CHILE",Cámara De Diputados| FHD | Valparaíso
http://camara.03.cl.cdnz.cl/camara19/live/chunklist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/fUQEubL.png" group-title="CHILE",Retro Plus | HD | Chile-Perú
https://59f1cbe63db89.streamlock.net:1443/retroplustv/_definst_/retroplustv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/fUQEubL.png" group-title="CHILE",Retro Plus 2 | HD | Chile-Perú
https://59f1cbe63db89.streamlock.net:1443/retroplussenal2/_definst_/retroplussenal2/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/fUQEubL.png" group-title="CHILE",Retro Plus 3 | HD | Chile-Perú
https://59f1cbe63db89.streamlock.net:1443/retroplussenal3/_definst_/retroplussenal3/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/saLbzvM.png" group-title="CHILE",Iquique TV | HD | Iquique
https://marine2.miplay.cl/arcatel/iquiquetv720/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/FMFLFIL.png" group-title="CHILE",Atacama TV | HD | Copiapó
https://v2.tustreaming.cl/atacamatv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/aPA11ts.png" group-title="CHILE",Holvoet TV | SD | Copiapó
https://pantera1-100gb-cl-movistar.dps.live/holvoettv/holvoettv.smil/holvoettv/livestream3/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/ZSpzX1F.png" group-title="CHILE",TV Quinta Región | HD | Valparaíso
https://mediacpstreamchile.com:1936/8002/8002/chunklist_w1281292195.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/VsfXiJy.png" group-title="CHILE",Pop Media | HD | Santiago
https://v4.tustreaming.cl/poptv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/PDVNb9i.png" group-title="CHILE",Buin Somos Todos| HD | Buin
https://bst.buin.cl/0.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/hoYBepx.png" group-title="CHILE",Canal 5 | HD | Linares
https://unlimited10-cl.dps.live/tv5/tv5.smil/tv5/livestream1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/Iu3turn.png" group-title="CHILE",Ñublevisión | HD | Chillán
https://cdn.oneplaychile.cl:1936/regionales/nublevision.stream/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/cibYn6l.png" group-title="CHILE",Click TV | HD | Coronel
http://v2.tustreaming.cl/clicktv/tracks-v1a1/mono.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/jL7zgG5.png" group-title="CHILE",Tele Angol | HD | Angol
https://pantera1-100gb-cl-movistar.dps.live/teleangol/teleangol.smil/teleangol/livestream1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/phbDD2v.png" group-title="CHILE",Pucón TV | FHD | Pucón
https://unlimited1-cl-isp.dps.live/pucontv/pucontv.smil/pucontv/livestream2/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/GG8zE02.png" group-title="CHILE",T-Vinet | HD | Osorno
https://unlimited1-cl-isp.dps.live/inet2/inet2.smil/inet2/livestream1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/Vm9LuU5.jpg" group-title="CHILE",Décima TV| FHD | Ancud
http://unlimited10-cl.dps.live/decimatv/decimatv.smil/decimatv/livestream1/chunks.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/JHG0k6v.png" group-title="CHILE",Santa María Televisión | SD | Coyhaique
https://unlimited1-cl-isp.dps.live/smtv/smtv.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/VhOolgs.png" group-title="CHILE",El Pingüino | HD | Punta Arenas
http://streaming.elpinguino.com:1935/live/pinguinotv_720p/livestream.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/mjX7HC0.png" group-title="CHILE",Soberanía| HD | Punta Arenas
https://tls-cl.cdnz.cl/radiosoberania/live/chunklist_w1753930486.m3u8
#EXTINF:-1 tvg-logo="https://i.imgur.com/Vx20KSy.jpg" group-title="CHILE",Umag TV 2| HD | Punta Arenas
https://tls-cl.cdnz.cl/umag2/live/playlist.m3u8
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

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/mi.tv.epg.xmll"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/gatotv.com.epg.xml"')
print(banner)

with open('../CHILE.txt', errors="ignore") as f:
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
    "https://github.com/pendy99/iptv-epg/raw/main/iptv_channels_chile.m3u"
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
            channel_info = group_title_pattern.sub('group-title="CHILE"', channel_info)
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
    
    
 

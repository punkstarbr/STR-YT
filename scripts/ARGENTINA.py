#! /usr/bin/python3

banner1 = r'''
###########################################################################
#                                                                         #
#                                  >> https://github.com/guiworldtv       #
###########################################################################
#EXTM3U
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_1080p.m3u8
	
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_720p.m3u8
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL
https://cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all.m3u8
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL
https://s@cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all_1080p.m3u8
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA - SINAL ORIGINAL 2
https://s@cntlnk-main-edge-access.secure.footprint.net/entrypoint/c7_vivo01_dai_source-20001_all.m3u8
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-chno="98" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/0/0a/Logo_Televisi%C3%B3n_P%C3%BAblica_Argentina.png" group-title="Argentina",TV PUBLICA
http://tvstarlife.com:25461/live/geovany/geovany/338.m3u8
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 2 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/channel/UCs231K71Bnu5295_x0MB5Pg/live
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 3
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/user/TVPublicaArgentina/live
#EXTINF:-1 tvg-id="TVPublicaHD.ar" tvg-logo="https://lh3.googleusercontent.com/-x6JNcq2aLCg/YtQgLsrRQKI/AAAAAAAAAqo/_sLdYldWdig0bMS-zrJkYdyOnJJ6uvF6wCNcBGAsYHQ/h120/ver-tv-publica-canal-7-argentina-en-vivo.jpg" group-title="Argentina", TV PUBLICA 4
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/channel/UCaU_cKHQ4IFHvBzQ-tKS1-Q/live
#EXTINF:-1 tvg-id="ElNueve.ar" tvg-country="AR" tvg-logo="https://vignette.wikia.nocookie.net/logopedia/images/f/f7/Canal-nueve-ar2017.png" group-title="Argentina", CANAL 9 35.1 
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/manifest/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/0df6d88d-304a-4d15-9cf8-eab1bc9b5e45/3.m3u8
#EXTINF:-1 tvg-id="elnueve" tvg-id="nueve" tvg-logo="https://www.elnueve.com.ar/_next/image?url=%2Flogo%2FlogotipoC9.png&w=256&q=75" group-title="Argentina",El nueve 
https://2a1773fcc0c94a639b422d1cf7ba14b7.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/.m3u8
#EXTINF:-1 tvg-id="elnueve" tvg-id="nueve" tvg-logo="https://www.elnueve.com.ar/_next/image?url=%2Flogo%2FlogotipoC9.png&w=256&q=75" group-title="Argentina",El nueve 2
https://00475e6934d74fe48a80427567a45918.mediatailor.us-east-1.amazonaws.com/v1/master/4c8323052bc3dbd9aa2eba0b638d8495561e8377/JW-Octubre-Channel09/live/channel09/live.isml/b00d164f-be51-473e-a47c-b33aa1f44186.m3u8
#EXTINF:-1 tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png" , EL TRECE 
https://live-01-02-eltrece.vodgc.net/eltrecetv/index.m3u8|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
#EXTINF:-1 tvg-id="El Trece" group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/45/Eltrece_logotipo_2018.png" , EL TRECE 2
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v2a1/mono.m3u8|user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0
#EXTINF:-1 tvg-id="Telefe.ar" tvg-logo="https://lh3.googleusercontent.com/-b2keOX5lUv4/YUDkI5UqpzI/AAAAAAAAAOo/I1NXuVoeXKIG-zh2E3nh6QqvhjY_kpq4wCLcBGAsYHQ/w480/Telefe.png",Telefe HD 2
https://is-tucuman.cdn.rcs.net.ar/mnp/telefe_hls/playlist.m3u8
#EXTINF:-1 tvg-id="Telefe.ar"  tvg-logo="https://lh3.googleusercontent.com/-b2keOX5lUv4/YUDkI5UqpzI/AAAAAAAAAOo/I1NXuVoeXKIG-zh2E3nh6QqvhjY_kpq4wCLcBGAsYHQ/w480/Telefe.png",Telefe (INT) 3
http://tvstarlife.com:25461/live/geovany/geovany/315.m3u8
#EXTINF:-1 tvg-id="Telefe.ar" tvg-country="AR" tvg-logo="http://x.playerlatino.live/telefe.png" group-title="Argentina", TELEFE 4
https://delivery.cdn.rcs.net.ar/mnp/telefe_hls/playlist.m3u8
#EXTINF:-1 tvg-id="Telefe" tvg-id="Telefe.ar" tvg-logo="https://telefe-static.akamaized.net/media/18154476/logo-telefe-twitter.png" group-title="Argentina",TELEFE COM VPN
https://mitelefe.com/Api/Videos/GetSourceUrl/694564/0/HLS
#EXTINF:-1 tvg-id="Telefe.ar" tvg-country="AR" tvg-logo="http://x.playerlatino.live/telefe.png" group-title="Argentina", TELEFE COM VPN 2
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8
#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a7/Telefe_Logo.svg/1280px-Telefe_Logo.svg.png",TELEFE COM VPN 3
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8 
#EXTINF:-1  tvg-id="InformacionPeriodistica.ar" group-title="Argentina" tvg-logo="https://i.imgur.com/SQSu9M5.png",Informacion Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8
#EXTINF:-1  tvg-id="NETTVHD.ar" group-title="Argentina" tvg-logo="https://canalnet.tv/_templates/desktop/includes/img/_logo-alt.png",NET TV 
https://unlimited1-buenosaires.dps.live/nettv/nettv.smil/playlist.m3u8
#EXTINF:-1 tvg-id="Encuentro.ar" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logo_del_canal_Encuentro.svg/150px-Logo_del_canal_Encuentro.svg.png" group-title="Argentina", ENCUENTRO 
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/.m3u8
#EXTINF:-1 tvg-id="Encuentro.ar" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logo_del_canal_Encuentro.svg/150px-Logo_del_canal_Encuentro.svg.png" group-title="Argentina", ENCUENTRO 2
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/user/encuentro/live
#EXTINF:-1 tvg-id="InformacionPeriodistica.ar" tvg-logo="https://img.ip.digital/sites/default/files/styles/1_1_max_364px/theme/ip_theme/media/ip_logo.png?itok=gzTn1Jjd" group-title="Argentina", IP 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/c/IPNoticiasEnVivo/live
#EXTINF:-1 tvg-logo="https://www.ipuntotv.com/IMAGES/TN%20logo%20nuevo.png" group-title="Argentina" ,TN 
https://delivery.cdn.rcs.net.ar/mnp/tn_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/TN_todo_noticias_logo.svg/290px-TN_todo_noticias_logo.svg.png" group-title="Argentina",TN Noticias
http://45.90.105.74:25461/live/budtvsports/wTu27rKVNU/1811.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c5/Canal_26_logo_%282022%29.svg/588px-Canal_26_logo_%282022 %29.svg.png" group-title="Argentina",Canal 26
http://200.115.193.177:80/live/26hd-720/chunklist_w1196091674.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-1Ltvq4TxvzE/YT5D2UFQimI/AAAAAAAAALY/irH51w9AkSEys2-buTru_86k_O9u_e-AQCLcBGAsYHQ/w480/C5N.png" group-title="Argentina" , C5N 
https://delivery.cdn.rcs.net.ar/mnp/c5n_hls/playlist.m3u8
#EXTINF:-1 tvg-chno="103" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/C5N_%282017%29.png/606px-C5N_%282017 %29.png" group-title="Argentina",C5N
http://tvstarlife.com:25461/live/geovany/geovany/283.m3u8
#EXTINF:-1 tvg-id="CronicaTV.ar" tvg-logo="https://www.utpba.org/wp-content/uploads/2019/07/cronica-logo.jpg" group-title="Argentina" , CRONICA 
http://free.fullspeed.tv/iptv-query?streaming-ip=https://www.youtube.com/c/cronicatv/live
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Su_IBL7T52g/YT5AkN3JRrI/AAAAAAAAALI/lQnG3U9ltAk-ckyIPKFkXZieGUgHyX75QCLcBGAsYHQ/w480/A24.png" group-title="Argentina" , A 24 
https://delivery.cdn.rcs.net.ar/mnp/a24_hls/playlist.m3u8
#EXTINF:-1 tvg-chno="104" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/82/A24_%282019-1%29.png" group-title="Argentina",A24
http://tvstarlife.com:25461/live/geovany/geovany/313.m3u8
#EXTINF:-1 tvg-id="Canal26HD.ar" tvg-logo="https://plushlamour.com.ar/wp-content/uploads/2021/01/canal3-1.png" group-title="Argentina" , C26 
https://delivery.cdn.rcs.net.ar/mnp/canal26_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://cdn.cnn.com/cnn/.e/img/3.0/global/misc/cnn-logo.png" group-title="Argentina" , CNN 
https://delivery.cdn.rcs.net.ar/mnp/cnn_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-inqhqQZAAGQ/YUDp5oL3lxI/AAAAAAAAAPY/NmRDCbQRAusmLK-7egIs-op4_u1z12_gACLcBGAsYHQ/w480/AXN.png" group-title="Argentina" , AXN 
https://delivery.cdn.rcs.net.ar/mnp/axn_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/a/AVvXsEhc-UYX7Vn9Ua5K2M2L1pi_ssLWJDJcwsIlw2EG8_kwppO6GVLVEsAVlqRyIhCWjRbgljzMuDnbGHoVPVBA7S9EwhtstmaIVGrP06PLSwJRTKmeZeAtTO2eJrys8XT9VkzaNUxJo-9tmYK_pPUFTg-gtM5Tys8u8uw3kZwA6pt-j60950tzsbdvO9l-" group-title="Argentina" , TNT 
https://delivery.cdn.rcs.net.ar/mnp/tnt_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-iD3Pp52qkYE/YsDywQHYs6I/AAAAAAAAAm4/u0hKfVvSTSU-B-kLAy2QI7vSkMapQgbOACNcBGAsYHQ/h120/ver-space-en-vivo.jpg" group-title="Argentina" , SPACE 
https://delivery.cdn.rcs.net.ar/mnp/space_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-cK4WNqOob_w/YUDpdrZzvEI/AAAAAAAAAPQ/DY9_xUdMjn0yP7ZbOfweOMYBReirkQeUACLcBGAsYHQ/w480/AMC.png" group-title="Argentina" , AMC 
https://delivery.cdn.rcs.net.ar/mnp/amc_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-GO_4vazX3lo/Ys9KMwNGLmI/AAAAAAAAAp8/6SfRXjBNMUQzuoijUxzqi6MHtzazHKx5gCNcBGAsYHQ/h120/ver-universal-tv-en-vivo.jpg" group-title="Argentina" , Universal 
https://delivery.cdn.rcs.net.ar/mnp/universal_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_fx_m.png" group-title="Argentina" , FX 
https://delivery.cdn.rcs.net.ar/mnp/fx_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://w7.pngwing.com/pngs/722/1014/png-transparent-logo-warner-bros-others-emblem-company-logo-thumbnail.png" group-title="Argentina" , WARNER 
https://delivery.cdn.rcs.net.ar/mnp/warner_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://static.wikia.nocookie.net/logopedia/images/6/61/Sony_Channel_2019.svg/revision/latest/scale-to-width-down/200?cb=20200117013250&path-prefix=es" group-title="Argentina" , SONY 
ttps://delivery.cdn.rcs.net.ar/mnp/sony_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://i.pinimg.com/originals/4b/ab/54/4bab54bc7bad8e728654032c5c817154.png" group-title="Argentina" , CINECANAL 
https://delivery.cdn.rcs.net.ar/mnp/cinecanal_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://media-exp2.licdn.com/dms/image/C560BAQHQ303-nahsMQ/company-logo_200_200/0/1593608716508?e=2147483647&v=beta&t=jIwFx63mao3NBPEYBn-_hS--cPrx5bT5h0jUL6jlAto" group-title="Argentina" , HBO 
https://delivery.cdn.rcs.net.ar/mnp/hbo_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_hbo-2_m.png" group-title="Argentina" , HBO 2 
https://delivery.cdn.rcs.net.ar/mnp/hbo2_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/HBO_Plus.png/640px-HBO_Plus.png" group-title="Argentina" , HBO PLUS 
https://delivery.cdn.rcs.net.ar/mnp/hboplus_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://cdn.mitvstatic.com/channels/ar_max-up_m.png" group-title="Argentina" , HBO POP 
https://delivery.cdn.rcs.net.ar/mnp/hbopop_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="http://1.bp.blogspot.com/-GGsnT8OYxqU/UJv5NAiymbI/AAAAAAAAXMo/3iytiCwX69s/s1600/isat.jpg" group-title="Argentina" , ISAT h
ttps://delivery.cdn.rcs.net.ar/mnp/isat_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-NDwbXJHYJMc/YT5RpJxdtpI/AAAAAAAAAOY/D1VEo88C3jwfky5Oiwww9TZX3ehLWpSfQCLcBGAsYHQ/w480/Cinemax.png" group-title="Argentina" , CINEMAX 
https://delivery.cdn.rcs.net.ar/mnp/cinemax_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-DRmD9dsKTi0/Ys9XhEvF5uI/AAAAAAAAAqM/NSP5eDAuKuAbbcfdah2I4rVpOvdSWahywCNcBGAsYHQ/w480/ver-tbs-en-vivo.jpg" group-title="Argentina" , TBS 
https://delivery.cdn.rcs.net.ar/mnp/tbs_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Riqq0wkw9UY/YT5RS6UxToI/AAAAAAAAAOQ/yfkgOB2YSOc_-xEiyvrq96QSYBgcQD8WACLcBGAsYHQ/w480/TCM.png" group-title="Argentina" , TCM 
https://delivery.cdn.rcs.net.ar/mnp/tcm_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjyhWjRQbbj9z-e8f_ZdUMB3negMEUlb6q6Rraql-rEHDRIyJTmGUOH5PI3DlCYmUlTy98H68aKLturEdTjDEIGTsytYLV6xBXXLw9etv1ggELuhXd2llW_86v27dpBoDnx9xQkHEcI2I37-q6uVdPcu0Kocm15ApYAoT2-IVIS7UevH2coIZF0vKDG/w480/ver-syfy-en-vivo.jpg" group-title="Argentina" , SYFY 
https://delivery.cdn.rcs.net.ar/mnp/syfy_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://assets3.cbsnewsstatic.com/hub/i/r/2022/02/15/352f4601-c86b-4a90-96ab-cf9cee9ae351/thumbnail/640x274/bdf6b7a51fb96db68b221f8b8a0be974/logo.jpg" group-title="Argentina" , PARAMOUNT 
https://delivery.cdn.rcs.net.ar/mnp/paramount_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://exchange4media.gumlet.io/news-photo/98602-MTVlogo.jpg?w=400&dpr=2.6" group-title="Argentina" , MTV 
https://delivery.cdn.rcs.net.ar/mnp/mtv_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://pbs.twimg.com/profile_images/738838081122541568/Xly8mKUw_400x400.jpg" group-title="Argentina", HTV 
https://delivery.cdn.rcs.net.ar/mnp/htv_hls/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d0/Logocmtvargentina.png" group-title="Argentina", CM 
https://delivery.cdn.rcs.net.ar/mnp/cm_hls/playlist.m3u8
'''


banner2 = r'''
#EXTINF:-1 tvg-logo="https://i.imgur.com/srtddlN.png" group-title="Argentina",TV Publica
https://delivery.cdn.rcs.net.ar/mnp/tvp/output.mpd
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Telefe_%28nuevo_logo%29.png/800px-Telefe_%28nuevo_logo%29.png"group-title="Argentina",TELECOLORMUX
https://live.obslivestream.com/telecolormux/tracks-v1a1/mono.m3u8
#EXTINF:-1 group-title="Argentina" tvg-logo="https://yt3.ggpht.com/ytc/AKedOLSYU51c8SbrkWZeNBRMFeCnGv0YXPpXuEGBNq-X5g=s88-c-k-c0x00ffffff-no-rj",Encuentro
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Encuentro.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-TgZv-RGCYoc/XrYHwcpfivI/AAAAAAAA0gw/AuqgxhioqLc1qhSHFDdH1ZftA0PKvOnzQCK8BGAsYHg/s0/2020-05-08.jpg" group-title="(CABLE)", 9LINK CHACO 
http://201.217.245.41:8081/testmelucas/canal9/playlist.m3u8
#EXTINF:-1 group-title="Argentina",el siete (tv publica)
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal7.m3u8
#EXTINF:-1 group-title="Argentina",EL NUEVE HD
https://raw.githubusercontent.com/fgillusi/IPTV-Argentina/main/Canal9.m3u8
#EXTINF:-1 group-title="Argentina",encuentro
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/playlist.m3u8
#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png", IP  24.5         
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8
#EXTINF:-1 group-title="Argentina" tvg-logo="http://www.grupocronica.com.ar/mediakit/wp-content/uploads/2017/10/cronica-hd-con-sombra-grande.png" , CRONICA HD  24.4
https://g5.vxral-slo.transport.edge-access.net/b10/ngrp:cronicatv_video1-100044_all/cronicatv_video1-100044_720p/index.m3u8
#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/LogoCanal26.png/120px-LogoCanal26.png" , CANAL 26  24.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w794690609_b2628000_sleng.m3u8
#EXTINF:-1 group-title="Argentina" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/A24_%282019-1%29.png/150px-A24_%282019-1%29.png" , A24  36.3
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056_720p.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png" group-title="Argentina", AMERICA HD  36.1
https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b0/Canal9.jpg" group-title="Argentina", CANAL 9  35.1 
https://ar-elnueve-elnueve-live.ned.media/live.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjI5NDY0OTI5LCJzZXNzaW9uIjoiMTgxLjQ0LjEyOS43MSIsIndoaXRlbGlzdCI6WyIxODEuNDQuMTI5LjcxIl19LCJzaWduYXR1cmUiOiJjNzQ2NTZjMjM0MjI5MmYwMDBhMzExZjNlYWIzMzBlNzVmYjJmNzY1In0=
#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5f523aa5523ae000074745ec/colorLogoPNG.png" group-title="Argentina" group-title="NEWS WORLD", TELEFÉ NOTICIAS
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5f523aa5523ae000074745ec/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff334c2-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=dffc36b9-57c6-4973-9903-2f83d465ac40&userId=&serverSideAds=true
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8f/Canal13_logo.png" group-title="Argentina", CANAL 13  33.1
http://edge5-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD-avc1_379968=10016.m3u8
#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="Argentina", SSIPTV ARG TV
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee700e0c&userId=&serverSideAds=true
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="Argentina", NET TV  27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Paka-paka.svg/245px-Paka-paka.svg.png" group-title="Argentina", PAKA PAKA  22.2
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_The_Simpsons.svg/1200px-Logo_The_Simpsons.svg.png" group-title="Argentina", LOS SIMPSONS
https://videostreaming.cloudserverlatam.com/cloudservertv/cloudservertv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/Logomagic96.png" group-title="Argentina", MAGIC KIDS
https://live.admefy.com/live/clean_peach_ef224.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Cine.Ar_logo.svg/1280px-Cine.Ar_logo.svg.png" group-title="Argentina", CINEAR  22.4
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8   
#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5de91cf02fc07c0009910465/colorLogoPNG.png" group-title="Argentina", TELEFÉ CLÁSICO
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5de91cf02fc07c0009910465/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1ae23-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=a367d0d9-b23d-4bb5-8d48-55f0cbeac4fb&userId=&serverSideAds=true
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/gwVNQhVICXN4Q7djaLyeQGCiMAa4Jum_PqeVaFZ1W90T4Y0G297wC1upnHRcKUbA6Q=w412-h220-rw" group-title="Argentina", GEN TV  17.3
https://videohd.live:19360/8010/8010.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Od4eldPqILM/XjtCKHxeYSI/AAAAAAAAvok/HDnuaXs9cCsFzbr0QrQtw3bYeDB0_5osACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", CINCO TV TIGRE  30.1
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8
#EXTINF:-1 tvg-logo="https://neotvdigital.com.ar/imagenes/logo1.png" group-title="Argentina", NEO TV DIGITAL  14.1
https://videostream.shockmedia.com.ar:19360/neotvdigital/neotvdigital.m3u8
#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="Argentina", CANAL 4 TELEAIRE SAN MARTIN
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8
#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VIC2PROV.png" group-title="Argentina", PROVINCIAL TV
http://www.trimi.com.ar/provincial/streaming/mystreamProvincialHSMed.m3u8
#EXTINF:-1 tvg-logo="http://www.canalkzo.com/images/lg_kzo.svg" group-title="Argentina", KZO
http://g2.vxral-slo.transport.edge-access.net/nx-beta/nx.hor.livetx.01/5eaa642772b3a25e2c28699e_540p/index.m3u8
#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-2gN4wEv_qPI/XjtKDwMuIQI/AAAAAAAAvrY/VTtJwZALBykDRnM8ia0Xbqi0FbREvdrZACK8BGAsYHg/s0/2020-02-05.png" group-title="Argentina", GARAGE TV
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist_w2049053275_b1296000_sleng.m3u8
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/150px-Deutsche_Welle_symbol_2012.svg.png" group-title="Argentina" group-title="NEWS WORLD", DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/stream05/streamPlaylist.m3u8
#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/mirador.png" group-title="Argentina", MIRADOR  22.3
https://5fb24b460df87.streamlock.net/live-cont.ar/mirador/playlist.m3u8 
#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4c/Telemax.png" group-title="Argentina", TELEMAX  26.3
https://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://d2ucqd3jt48qxz.cloudfront.net/img/footer-logo.png" group-title="Argentina", ORBE 21  21.2
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8
#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="Argentina", UNIFE TV  25.1
https://dacastmmd.mmdlive.lldns.net/dacastmmd/98adedd6dec04a2d8663899b927f9383/chunklist_b4628000.m3u8
#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VISANTAM.png" group-title="Argentina", SANTA MARIA
http://www.trimi.com.ar/santa_maria/streaming/mystreamSantaMariaHSMed.m3u8
#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8
#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"
#EXTM3U
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://200.115.193.177/live/26hd-720/.m3u8?CompartilhandoIPTV
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26  (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 (San Justo-Arg.)
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w858131162_b414000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://uni5rtmp.tulix.tv:1935/bettervida/bettervida/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://azxtv.com/hls/stream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8204/8204/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://stmv4.questreaming.com/fenixlarioja/fenixlarioja/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/madryntv/madryntv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://arcast.net:1935/mp/mp/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://200.115.193.177/live/26hd-720/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.dattalive.com/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://s8.stweb.tv/chacra/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://coninfo.net:1935/chacodxdtv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream102.akamaized.net/hls/live/2015525/dwstream102/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/index.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://euronews-euronews-spanish-2-mx.samsung.wurl.com/manifest/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://panel.dattalive.com:1935/8250/8250/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stream.live.novotempo.com/tv/smil:tvnuevotiempo.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/live-powerTV/power.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://rbmn-live.akamaized.net/hls/live/590964/BoRB-AT/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.trimi.com.ar/santa_maria/streaming/mystream.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://panel.seo.tv.bo:3337/live/franzbalboa2live.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tastemade-es8intl-roku.amagi.tv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://wowza.telpin.com.ar:1935/telpintv/ttv.stream/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://tv-trtworld.live.trt.com.tr/master.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
http://cdnh4.iblups.com/hls/irtp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://america-crtvg.flumotion.com/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://stratus.stream.cespi.unlp.edu.ar/hls/tvunlp.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://59a564764e2b6.streamlock.net/vallenato/Vallenato2/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal Nueve Multivisi n (AR)
https://5f700d5b2c46f.streamlock.net/vertv/vertv/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top  (Argentina)
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax  HD Argent.
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/chunklist_w950122583_b1828000_sleng.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",24/7 Canal de Noticias
http://59c5c86e10038.streamlock.net:1935/6605140/6605140/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5RTV Santa Fe
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV (Corrientes) (480p)
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",5TV Corrientes
http://www.coninfo.net:1935/tvcinco/live1/chunklist_w1546509083.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",CANAL PROVINCIAL SAN MIGUEL
http://www.trimi.com.ar/provincial/streaming/mystream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-180/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://200.115.193.177/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-360/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/26hd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26
http://live-edge01.telecentro.net.ar:1935/live/26hd-720/livestream.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Chacra TV
http://s8.stweb.tv:1935/chacra/live/chunks.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Ciudad TV Chaco
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music TOP
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w1582140541_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/musictop.smil/.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/chunklist_w538311571_b364000_sleng.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Music Top
http://live-edge01.telecentro.net.ar:1935/live/msctphd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/tlxhd-720/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",TLX
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/master.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Telemax
http://live-edge01.telecentro.net.ar/live/tlxhd-720/playlist.m3u8?checkedby:iptvcat.com
#EXTINF:-1  tvg-id="277" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/277_Canal_XFN.png",Canal XFN * | AR
https://streamconex.com:1936/canalxfn/canalxfn/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1026" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1026_Tele_Mix.png",Tele Mix * | AR
https://panel.dattalive.com:443/8068/8068/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="488" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/488_Anime_Zone_TV.png",Anime Zone TV | AR
http://azxtv.com/hls/stream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="206" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/206_Paka_Paka.jpg",Paka Paka | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="251" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/251_13_Max_Television.png",13 Max Television | AR
http://coninfo.net:1935/13maxhd/live13maxtvnuevo_720p/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="221" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/221_5R_TV_Santa_Fe.png",5R TV Santa Fe | AR
http://api.new.livestream.com/accounts/22636012/events/8242619/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="249" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/249_5TV.png",5TV | AR
http://www.coninfo.net:1935/tvcinco/live1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="252" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/252_Aire_de_Santa_Fe.png",Aire de Santa Fe | AR
https://sc1.stweb.tv/airedigital/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="215" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/215_Azahares_Radio_Multimedia.png",Azahares Radio Multimedia | AR
http://streamyes.alsolnet.com/azaharesfm/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="224" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/224_Cadena_103.png",Cadena 103 | AR
http://arcast.net:1935/cadena103/cadena103/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="799" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/799_Canal_10_Nortevision.jpg",Canal 10 Nortevision | AR
https://vivo.solumedia.com:19360/nortevision/nortevision.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="299" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/299_Canal_10_Rio_Negro.png",Canal 10 Rio Negro | AR
https://panel.dattalive.com:443/8204/8204/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="268" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/268_Canal_12_Madryn_TV.png",Canal 12 Madryn TV | AR
https://5f700d5b2c46f.streamlock.net:443/madryntv/madryntv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="227" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/227_Canal_13_La_Rioja.jpg",Canal 13 La Rioja | AR
http://arcast.net:1935/mp/mp/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="228" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/228_Canal_2_Jujuy.png",Canal 2 Jujuy | AR
http://api.new.livestream.com/accounts/679322/events/3782013/live.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="205" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/205_Canal_2_Sanagasta.jpg",Canal 2 Sanagasta | AR
https://stmvideo1.livecastv.com/canal2/canal2/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="229" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/229_Canal_20_Villamaria.png",Canal 20 Villamaria | AR
https://cronos.aldeaglobal.net.ar/hls/canal20.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1057" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1057_Canal_21_TV.png",Canal 21 TV | AR
https://iptv.ixfo.com.ar:30443/c21tv/hd/c21tv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="230" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/230_Canal_22_Buenos_Aires.jpg",Canal 22 Buenos Aires | AR
https://5f700d5b2c46f.streamlock.net:443/canal22/canal22/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="271" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/271_Canal_26.png",Canal 26 | AR
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",Canal 26 HD (AR)
https://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist.m3u8?ROGERIOTORRES
#EXTINF:-1  tvg-id="256" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/256_Canal_3_Rosario.png",Canal 3 Rosario | AR
https://59d52c5a5ce5e.streamlock.net:4443/canal3rosario/ngrp:canal3rosario_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="257" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/257_Canal_4_Bahia_Blanca.png",Canal 4 Bahia Blanca | AR
https://vivo.solumedia.com:19360/bvconline/bvconline.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="258" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/258_Canal_4_Jujuy.png",Canal 4 Jujuy | AR
http://190.52.32.13:1935/canal4/smil:manifest.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="259" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/259_Canal_4_Posadas.png",Canal 4 Posadas | AR
http://iptv.ixfo.com.ar:8081/live/C4POS/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="233" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/233_CANAL_5TV.jpg",CANAL 5TV | AR
https://srv3.zcast.com.br/carlosr/carlosr/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="307" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/307_Canal_6_Entre_Rios.png",Canal 6 Entre Rios | AR
https://stmvideo1.livecastv.com/canal6er/canal6er/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="262" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/262_Canal_6_Posadas.png",Canal 6 Posadas | AR
https://iptv.ixfo.com.ar:30443/live/c6digital/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="264" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/264_Canal_7_Jujuy.png",Canal 7 Jujuy | AR
https://stream.arcast.live/canal7jujuy/ngrp:canal7jujuy_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="236" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/236_Canal_9_Litoral.png",Canal 9 Litoral | AR
https://stream.arcast.live/ahora/ahora/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="273" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/273_Canal_907_FM_Comunicar.png",Canal 907 FM Comunicar | AR
https://panel.dattalive.com/canal907/canal907/chunklist_w1205944599.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="274" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/274_Canal_Cinco_Tigre.png",Canal Cinco Tigre | AR
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="275" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/275_Canal_Coop.png",Canal Coop | AR
https://panel.dattalive.com:443/8138/8138/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="302" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/302_Canal_Nueve_TV.png",Canal Nueve TV | AR
https://live.canalnueve.tv/canal.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="801" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/801_Canal_Provincial.jpg",Canal Provincial | AR
https://streaming.telered.com.ar/provincial/streaming/mystream.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="278" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/278_Chacra_TV.png",Chacra TV | AR
https://s8.stweb.tv/chacra/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="237" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/237_Ciudad_TV.jpg",Ciudad TV | AR
http://coninfo.net:1935/chacodxdtv/live/chunklist_w1251301598.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="280" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/280_CL3_Cablevision.png",CL3 Cablevision | AR
http://videostream.shockmedia.com.ar:1935/cl3cable/cl3cable/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="270" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/270_CN_24_7_Neuquen.png",CN 24/7 Neuquen | AR
https://panel.dattalive.com:443/6605140/smil:6605140.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="893" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/893_Complejo_Dance.png",Complejo Dance | AR
https://mediacp.hostradios.com.ar:19360/complejodance/complejodance.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="238" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/238_CPE_TV.jpg",CPE TV | AR
https://stream.arcast.live/cpe/ngrp:cpe_all/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="239" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/239_Fenix.jpg",Fenix | AR
https://stmvideo1.livecastv.com/fenixlarioja/fenixlarioja/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="803" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/803_FM_Metropolitana_100_5_MHZ.png",FM Metropolitana 100.5 MHZ | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="216" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/216_Informacion_Periodistica.jpg",Informacion Periodistica | AR
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/5ee6e167-1167-4a85-9d8d-e08a3f55cff3.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="217" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/217_La_Voz_de_Tucuman.png",La Voz de Tucuman | AR
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="212" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/212_Link_TV.png",Link TV | AR
https://panel.dattalive.com:443/8128_1/8128_1/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="283" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/283_Metro_TV_Canal_12_Tucuman.png",Metro TV Canal 12 Tucuman | AR
https://streamtv12.ddns.net:5443/LiveApp/streams/193945633734205616732920.m3u8?token=null&PlaylistM3UCL
#EXTINF:-1  tvg-id="795" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/795_Metropolitana_FM.png",Metropolitana FM | AR
https://panel.dattalive.com/MetropolitanaFM/MetropolitanaFM/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="284" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/284_Multivision.png",Multivisi n | AR
https://panel.dattalive.com:443/8250/8250/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="285" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/285_Net_TV.png",Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="243" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/243_Power.png",Power | AR
https://live2.tensila.com/1-1-1.power-tv/hls/master.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="912" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/912_Radio_Blu.png",Radio Blu | AR
https://59537faa0729a.streamlock.net:443/radioblu/radioblu/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="210" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/210_Radiocanal_San_Francisco.png",Radiocanal San Francisco | AR
http://204.199.3.2/.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="287" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/287_RTN.png",RTN | AR
http://media.neuquen.gov.ar/rtn/television/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="288" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/288_Sicardi_TV.png",Sicardi TV | AR
https://vivo.solumedia.com:19360/sicarditv/sicarditv.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="289" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/289_TDC_TV_Santa_Fe.png",TDC TV Santa Fe | AR
https://5e7cdf2370883.streamlock.net/tdconline/tdconline/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="308" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/308_Tele_Estrella.png",Tele Estrella | AR
https://stmvideo2.livecastv.com/telestrella/telestrella/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="290" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/290_Telecreativa.png",Telecreativa | AR
https://panel.dattalive.com:443/8012/8012/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="291" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/291_Telediario_Television.png",Telediario Televisi n | AR
https://mediacp.hostradios.com.ar:19360/telediario/telediario.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="245" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/245_Telediez.jpg",Telediez | AR
https://videohd.live:19360/8020/8020.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="292" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/292_Telemax.png",Telemax | AR
http://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="814" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/814_TeleNord.jpg",TeleNord | AR
http://www.coninfo.net:1935/previsoratv/live/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="293" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/293_Telpin_Canal_2.png",Telpin Canal 2 | AR
https://wowza.telpin.com.ar:1935/telpintv/smil:ttv.stream.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="294" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/294_Terramia_TV.png",Terramia TV | AR
https://live-edge01.telecentro.net.ar/live/smil:trm.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="296" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/296_TSN_Necochea.png",TSN Necochea | AR
https://panel.dattalive.com:443/tsnnecochea/tsnnecochea/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="788" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/788_TV_Dos_Salta.jpg",TV Dos Salta | AR
https://vivo.solumedia.com:19360/tv2salta/tv2salta.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="248" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/248_Uni_Teve.png",Uni Teve | AR
https://vivo.solumedia.com:19360/uniteve/uniteve.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="493" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/493_Net_TV.png",Net TV | AR
https://unlimited1-cl-isp.dps.live/nettv/nettv.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="24" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/24_Music_Top.png",Music Top | AR
http://live-edge01.telecentro.net.ar/live/smil:musictop.smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="208" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/208_CINE_AR.png",CINE.AR | AR
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="207" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/207_Orbe_21.jpg",Orbe 21 | AR
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="1003" group-title="Argentina" tvg-logo="https://www.m3u.cl/logo/1003_Sublime_Gracia_TV.png",Sublime Gracia TV | AR
https://5f700d5b2c46f.streamlock.net:443/sublime/sublime/playlist.m3u8?PlaylistM3UCL
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="https://www.cxtv.com.br/img/Tvs/Logo/webp-l/d800ee1a28bbee6769de24c5c050c40c.webp",Canal Once
https://vivo.canaloncelive.tv/alivepkgr3/ngrp:cepro_all/playlist.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="N/A" tvg-logo="N/A",LA VOZ DE TUCUMAN
https://srv1.zcast.com.br/lavozdetucuman/lavozdetucuman/.m3u8
import requests
from bs4 import BeautifulSoup
import datetime
import streamlink
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True
for i in range(1, 6):
    url = f"https://tviplayer.iol.pt/videos/ultimos/{i}/canal:"

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
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
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://github.com/Nicolas0919/Guia-EPG/raw/master/GuiaEPG.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml.gz"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/directv.com.ar.epg.xml.gz"')
    video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
    video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
    Data = [item.text for item in soup.find_all("span", class_="item-date")]

print(banner1)
    for title, link in zip(video_titles, video_links):
        now = datetime.datetime.now()
        timestamp = now.strftime("%m%d%H%M%S")
        video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
        item = soup.find("a", class_="item", href=link)
        try:
            image_url = item["style"].split("url(")[1].split(")")[0]
        except Exception as e:
            print(f"Error: {e}")
            image_url = "https://cdn.iol.pt/img/logostvi/branco/tviplayer.png"
        if video_url:
            m3u8_file.write(f"#EXTINF:-1 group-title=\"TVI PLAYER\" tvg-logo=\"{image_url}\",{title}\n{video_url}\n")
            m3u8_file.write("\n")

#s = requests.Session()
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


time.sleep(13)

m3u8_file.close()

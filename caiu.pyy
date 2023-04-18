import os
import sys
import pytz
import datetime

# Instala bibliotecas necessárias se não estiverem presentes
try:
    import streamlink
except ImportError:
    os.system("pip install --user --upgrade streamlink")

try:
    import youtube_dl
    import requests
    import beautifulsoup4
    import fastapi
    import uvicorn
    import schedule
    import selenium
except ImportError:
    os.system("pip install youtube-dl requests beautifulsoup4 fastapi uvicorn schedule selenium datetime")

# Autenticação do usuário com as credenciais do Codespaces Secrets
api_key = os.environ.get('APIGOOGLEDRIVE')
creds = None
if api_key:
    creds = api_key
else:
    creds, _ = google.auth.default()
service = build("drive", "v3", credentials=creds)

def create_folder(folder_name):
    """Cria uma nova pasta no Google Drive"""
    try:
        file_metadata = {
            'name': folder_name,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=file_metadata, fields='id').execute()
        print(F'Pasta criada com o ID: {folder.get("id")}')
        return folder.get('id')
    except HttpError as error:
        print(F'Ocorreu um erro ao criar a pasta: {error}')
        return None

def upload_to_folder(file_path, file_name, folder_id):
    """Faz upload do arquivo para a pasta especificada"""
    try:
        file_metadata = {'name': file_name, 'parents':[folder_id]}
        media = MediaFileUpload(file_path, mimetype='video/MP2T')
        file = service.files().create(body=file_metadata, media_body=media,
                                      fields='id').execute()
        print(F'File ID: {file.get("id")}')
    except HttpError as error:
        print(F'Ocorreu um erro: {error}')
        file = None
    return file

def main():
    # Obtenha a hora atual no fuso horário de São Paulo
    tz = pytz.timezone("America/Sao_Paulo")
    hora_atual = datetime.datetime.now(tz).strftime("%d%m_%H%M%S")

    # Grava streams usando streamlink
    streamlink_command_1 = "streamlink --force --hls-duration 00:04:00 --output "
    streamlink_command_1 += f"\"GRAVADOS/{hora_atual}_CBSTELEMUNDO_.ts\" https://www.youtube.com/@TelemundoEntretenimiento/live best"
    os.system(streamlink_command_1)

    streamlink_command_2 = "streamlink --force --hls-duration 00:07:00 --output "
    streamlink_command_2 += f"\"GRAVADOS/{hora_atual}_CBSNEWS_.ts\" https://www.cbsnews.com/live/ best"
    os.system(streamlink_command_2)

    streamlink_command_3 = "streamlink --force --hls-duration 00:07:00 --output "
    streamlink_command_3 += f"\"GRAVADOS/{hora_atual}_CNNPORTUGAL.ts\" https://tviplayer.iol.pt/direto/CNN best"
    os.system(streamlink_command_3)

if __name__ == "__main__":
    main()

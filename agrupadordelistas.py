import glob
import os

# Obter o caminho do arquivo atual
file_path = os.path.dirname(os.path.realpath(__file__))

# Verificar se o arquivo LISTASAGRUPADAS.m3u8 já existe
file_to_merge = os.path.join(file_path, "LISTASAGRUPADAS.m3u8")
if os.path.exists(file_to_merge):
    if not os.remove(file_to_merge):
        print("Erro ao excluir o arquivo: ", file_to_merge)
else:
    print("O arquivo {} não existe".format(file_to_merge))

# Obter todos os arquivos .m3u na pasta
source_files = sorted(glob.glob(os.path.join(file_path, "*.m3u")))

# Imprimir a lista de arquivos encontrados
print("Arquivos encontrados:", source_files)

# Abrir o arquivo de saída para escrita
with open(file_to_merge, "wb") as merged_file:
    for file in source_files:
        # Abrir o arquivo de entrada para leitura
        with open(file, "rb") as source_file:
            # Adicionar uma linha em branco entre cada arquivo
            merged_file.write(b"\n")
            # Copiar o conteúdo do arquivo de entrada para o arquivo de saída
            merged_file.write(source_file.read())
            
            



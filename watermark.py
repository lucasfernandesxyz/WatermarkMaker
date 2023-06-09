import os
from PIL import Image

# arquivo de marca dagua
watermark_file = r"watermark.png"

# entrada dos videos
input_directory = r"content"

# saida dos vídeos
output_directory = r"converted"


# ======= Video =======


# Loop para percorrer os arquivos .mp4 no diretório de entrada
for filename in os.listdir(input_directory):
    if filename.endswith(".mp4"):
        input_file = os.path.join(input_directory, filename)
        filename_without_extension = os.path.splitext(filename)[0]
        output_file = os.path.join(output_directory, f"{filename_without_extension}-watermarked.mp4")

        # Comando ffmpeg para adicionar marca d'água com transparência de 50%
        command = f'ffmpeg -i "{input_file}" -i "{watermark_file}" -filter_complex "[0:v][1:v] overlay=main_w-overlay_w-5:main_h-overlay_h-5:format=auto,format=yuv420p" -codec:a copy "{output_file}"'

        # Executa o comando no terminal
        os.system(command)


#======= Fotos =======

# Llsta todos os arquivos do diretório de entrada
files = os.listdir(input_directory)

# Loop para percorrer os arquivos no diretório de entrada
for file in files:
    input_file = os.path.join(input_directory, file)

    # verifica se o arquivo é uma imagem (suportada pelo PIL)
    if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp")):
        # Caminho completo para o arquivo de saída
        output_file = os.path.join(output_directory, file)

        # Abre a imagem de origem
        imgS = Image.open(input_file).convert("RGBA")

        # Abre a imagem da marca d'água
        watermark = Image.open(r"watermark.png")

        # Aplica a marca d'água na imagem de origem
        imgS.paste(watermark, (0, 0), watermark.convert("RGBA"))

        # Salva a imagem convertida
        imgS.save(output_file, format="png", quality=90)

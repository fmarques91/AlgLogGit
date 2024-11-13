from moviepy.editor import VideoFileClip
import os

# Caminho para o arquivo do vídeo
# caminhoVideo = "EngenhariaDeSoftware_2024-10-29.mp4"
diretorioAtual = os.getcwd()

conteudo = os.listdir(diretorioAtual)

arquivos = []
print('=-' * 20)
for item in conteudo:
    print(item)
    arquivos.append(item)
print('=-' * 20)


opcao = int(input('Digite a opção conrrespondente ao vídeo: '))
caminhoVideo = arquivos[opcao - 1]

#Caminho para saída do audio / Tentar incluir um imput para nomear manualmente a saída.
saidaAudioMp3 = "Audio Extraido.mp3"

#Carrega o vídeo em uma variável, utilizando a função "VideoFileClip" e incluindo entre parenteses o caminho do arquivo
video = VideoFileClip(caminhoVideo)

# ".audio" extrai o audio do vídeo e armazena na variável audio
audio = video.audio

#Salva o arquivo em áudio, utilizando a variável contendo o áudio, a função ".write_audiofile" e entre parenteses o caminho de saída
audio.write_audiofile(saidaAudioMp3)

# Fecha a variável contendo o vídeo e a variável contendo o audio, para economia de memória.
video.close()
audio.close()
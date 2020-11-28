import os
from funcoes.constantes import COR
from funcoes.constantes import DIRECAO as DIR
from time import localtime, strftime

#Resolução do vídeo analisado
RESOLUTION = {
    'width': int(640),      #Largura do vídeo
    'height': int(480),     #Altura  do vídeo
}

#VIDEO_NAME = "C:\Users\marll\Desktop\contador_de_carros\contador de carros\video.mp4" #nome do vídeo analisado


SHOW_TRACES = True          #Se for Verdadeiro, todas as linhas e quadrados de identificação serão desenhados na tela

FRAME_CHECK = 1             #Identifique objetos na tela a cada 10 quadros (padrão)

RECORDING = False           #Se você quiser salvar a imagem de teste, mude para verdadeiro

MIN_SCORE = 0.4             #Score mínimo para seleção

CLASSES = {                 #A classe que o modelo reconhecerá
    'carro': 1.0,
}

COR_CLASSE = {
    '1': COR['azul'],
}

MODEL_NAME = "modelo_marllon" #Modelo que será usado para a análise

#Não modifique os valores das seguintes variáveis, porque eles são apenas que seus valores são 
# É composto pelos valores das variáveis ​​acima e pode ser modificado 

FULL_RESOLUTION = (RESOLUTION['width'], RESOLUTION['height'])

EXECUTION_PATH = os.getcwd()

#Considere que o arquivo de saída retorna um nome diferente 
# Data e hora de início da gravação
def name_video_out():
    prefix = EXECUTION_PATH + "/video_out/out_"
    str_date = strftime("%d-%m-%Y_%H:%M:%S", localtime())
    name_video = prefix + str_date + ".mp4"
    return name_video
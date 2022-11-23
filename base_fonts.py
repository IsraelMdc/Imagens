import os
from random import randint
from PIL import ImageFont, ImageDraw, Image
import cv2
import numpy as np
import glob

image = cv2.imread("Me.jpg")
cv2_im_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
pil_im = Image.fromarray(cv2_im_rgb)
draw = ImageDraw.Draw(pil_im)
path = "/home/palestina/Desktop/TESTES/Imagens/fontes/*"
listadefonte = glob.glob(path)
font = randint(0,len(listadefonte)-1)
alphafont =(listadefonte[font])
betafont = ImageFont.truetype("{}".format(alphafont), 80)
draw.text((10, 700), "to puto com esses heteros falando atras de mim", font= betafont, align="center")
cv2_im_processed = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)
cv2.imshow('Fonts', cv2_im_processed)


import random
import cv2
from english_words import english_words_set
import numpy as np


def text():




qtd = 10

palavras = (random.sample(english_words_set,qtd))
print (palavras)


for palavra in palavras:
    d_tela = 50, 100, 3
    blank = 255*np.ones((d_tela)).astype(np.uint8)
    img = blank
    tamanho_fonte = random.randint(3, 5)
    textsize = cv2.getTextSize(palavra, cv2.FONT_HERSHEY_SIMPLEX, tamanho_fonte,  2)[0]
    textX = int((900 -textsize[0])/2)
    textY = int((300 - textsize[1])/2)
    ax = random.randint(-5,5)/100
    ay =  random.randint(-5,5)/100
    x = int(textX + (ax*900))
    y = int(textY + (ay*300))
    print(textsize, textX, textY, x, y, ax, ay)
    palavra = str(palavra)
    cv2.putText(img, palavra, (x, y), cv2.FONT_HERSHEY_SIMPLEX, tamanho_fonte, (000, 000, 000, 000), 2)
    cv2.imshow('tela',img)
    cv2.imwrite(f'{palavra}.png', blank)
    cv2.waitKey(0)
    
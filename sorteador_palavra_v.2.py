import random
import cv2
from english_words import english_words_set
import numpy as np
from PIL import ImageFont, ImageDraw, Image
import glob

qtd = 3
fontsize = 1
palavras = (random.sample(english_words_set, qtd))
for palavra in palavras:
    palavra = str(palavra)
    h, w = 100, 300
    blank = 255*np.ones((h, w)).astype(np.uint8)
    image_pil = Image.fromarray(blank)
    draw = ImageDraw.Draw(image_pil)
    fonts = glob.glob("/home/palestina/Desktop/TESTES/Imagens/fontes/*")
    font = random.choice(fonts)
    font_pil = ImageFont.truetype(font, fontsize)
    img_fraction = 0.30
    font_pil = ImageFont.truetype(font, fontsize)
    while font_pil.getsize(palavra)[0] < img_fraction*300:
        fontsize += 1
        font_pil = ImageFont.truetype(font, fontsize)
    fontsize -= 1
    font_pil = ImageFont.truetype(font, fontsize)
    textsize = draw.textsize(palavra, font=font_pil)
    textX = int((300 -textsize[0])/2)
    textY = int((100 - textsize[1])/2)
    ax = random.randint(-5,5)/100
    ay =  random.randint(-5,5)/100
    x = int(textX + (ax*300))
    y = int(textY + (ay*100))
    rw = int((300*ax) + 300)
    rh = int((100*ay) + 100)
    dim = (rw, rh)
    draw.text((x,y), palavra, font = font_pil, align="center")
    processed = cv2.cvtColor(np.array(image_pil), cv2.COLOR_RGB2BGR)
    cv2.resize(processed, dim)
    cv2.imshow('Image', processed)
    cv2.imwrite(f'{palavra}.png', processed)
'''
qtd = 10
palavras = (random.sample(english_words_set,qtd))
print (palavras)
#aleatórios
for palavra in palavras:
    d_tela = 300, 900, 3
    blank = 255*np.ones((d_tela)).astype(np.uint8)
    img = blank
    tamanho_fonte = random.randint(3, 5)
    textsize = cv2.getTextSize(palavra, cv2.FONT_HERSHEY_SIMPLEX,  2, 1)[0]
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
    cv2.imwrite('Me.png', blank)
    cv2.waitKey(0)
'''
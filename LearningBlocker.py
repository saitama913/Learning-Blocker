import cv2 as cv
import numpy as np
import random
from IPython.display import Image, display

#画像の読み込み
img = cv.imread('C:\\Users\\Misso\\Downloads\\computer_shigotoscreen_back_man.png')

width = img.shape[1]
height = img.shape[0]

#8*8行列の生成とランダムな透かし生成
LB = np.identitiy(8, dtype = None)
#穴の数をランダムで生成
ananokazu = random.randrange(64)
#穴の位置をランダムで指定しつつ透かしの濃さもランダムで指定
for i in range(ananokazu):
    a = random.randrange(8)
    b = random.randrange(8)
    noudo = random.randrange(256)
    LB[a,b] = noudo

#生成したランダム透かしを入力画像のサイズまで拡張
yoko = width/8
tate = height/8

sukashi1 = np.tile(LB, (yoko, tate, 3))
print(sukashi1)


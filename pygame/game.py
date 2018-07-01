#### 始めにモジュールのimport

import sys
import math
import pygame
from pygame.locals import QUIT

### pygameの初期化
pygame.init()

### 画面の設定。ここでは６００×６００に設定
size = (1200,900)
GAMEN = pygame.display.set_mode(size)

### キャプションの表示
pygame.display.set_caption("smallRedMonster")

### クロックの設定はpygame.time.Clock()で行う
CLOCK = pygame.time.Clock()

### main routineを　def main():と記述

def main(): ###以下、インデントが必要
    """ main routine """
    radius = 100
    y_center = 300 ### 円の中心座標ｙ
    x_center = 300 ### 円の中心座標ｘ

    count = 0
    
    a = math.pi/360
    deg = 0
    rad = 0

    ### キャラクターの呼び込み、コードと同じホルダーに記録が便利

    image = pygame.image.load("player.png")

    ### 以下がキャラクターを動かすコード。以下すべてインデントが必要。

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        #角度はラジアンで計算

        GAMEN.fill(0xFFFFFF)
        count += a/math.pi
        rad += count
        y = int(radius * math.sin(rad)) + y_center #yの座標
        x = int(radius * math.cos(rad)) + x_center #xの座標
        ### 画面にimageを表示。blitを用いる。
        GAMEN.blit(image,(x,y))
        ### 画面の初期化 
        pygame.display.update()
        ### タイム・ディレイの挿入
        CLOCK.tick(500)
        ### 角度の初期化
        if count >= math.pi/180 :
            count = 0

        ### runで動かす場合の常套句、コードの最後に記載 

if __name__ == '__main__':
    main()

### 
#!/usr/bin/python
# -*- Coding: utf-8 -*-

import os
import copy
import time
import sys
import random
import pygame
from pygame.locals import *

# メイン処理
def main():
    sort_arr = [8, 6, 4, 5, 7, 3, 1, 2]
    sel_arr = [0, 0, 0, 0, 0, 0, 0, 0]

    SORT_SPEED_SEC = 1
    CHECK_SPEED_SEC = 0.4
    start = False

    # pygame の初期化
    pygame.init()

    # 画面サイズを指定して、画面を生成
    screen = pygame.display.set_mode((800, 700))

    #タイトルバーに表示する文字
    pygame.display.set_caption("ソート・アルゴリズムを確認しよう | CoderDojo 太宰府")

    # 画面を黒く塗りつぶす
    screen.fill((0, 0, 0))

    # タイトル表示
    put_title(screen)

    # 盤面の更新
    put_frame(screen, sort_arr, sel_arr)

    # ここまでが初期処理で、ここからループし、画面をずっと表示する
    while (1):

        # 速度調整のsleep
        time.sleep(CHECK_SPEED_SEC)

        # キー入力などのイベント処理
        start = event_proc()
        if start:
            # ソート開始
            selectionSort(screen, sort_arr, sel_arr, SORT_SPEED_SEC)


# イベント処理
def event_proc() -> bool:
    # イベント処理
    for event in pygame.event.get():
        if event.type == QUIT:
            # 閉じるボタンが押されたら、pygameを終了
            pygame.quit()
            # pygame.quit()だけでもよさそうだが、正常終了するために書いておく
            sys.exit()
        elif event.type == KEYDOWN:
            # キーボードが押されたら
            if event.key == K_SPACE:
                return True
    return False


# ブロック画像を返す
def get_block_img(index: int):
    if index == -1:
        ret_img = pygame.image.load("./img/dot.png")
    elif index == 0:
        ret_img = pygame.image.load("./img/black.png")
    elif index == 1:
        ret_img = pygame.image.load("./img/1.png")
    elif index == 2:
        ret_img = pygame.image.load("./img/2.png")
    elif index == 3:
        ret_img = pygame.image.load("./img/3.png")
    elif index == 4:
        ret_img = pygame.image.load("./img/4.png")
    elif index == 5:
        ret_img = pygame.image.load("./img/5.png")
    elif index == 6:
        ret_img = pygame.image.load("./img/6.png")
    elif index == 7:
        ret_img = pygame.image.load("./img/7.png")
    elif index == 8:
        ret_img = pygame.image.load("./img/8.png")
    else:
        ret_img = pygame.image.load("./img/original.png")
    return ret_img


# タイトル表示用
def put_title(screen):
    # フォントの生成
    font = pygame.font.Font(None, 40)
    screen.blit(font.render("Press SPACE KEY to start Selection Sort", True, (0, 255, 0)), [60, 50])

    screen.blit(font.render("Selection:", True, (0, 255, 0)), [60, 580])
    screen.blit(font.render("Swap:", True, (0, 255, 0)), [400, 580])
    # 画面を更新
    pygame.display.update()


# 盤面の更新
def put_frame(screen, sort_arr, sel_arr):
    x = 1
    for a in sort_arr:
        block_img = get_block_img(int(a))
        screen.blit(block_img, (60 * x, 100))
        x += 1
    x = 1
    for a in sel_arr:
        block_img = get_block_img(int(a))
        screen.blit(block_img, (60 * x, 500))
        x += 1
    # 画面を更新
    pygame.display.update()


# カウント表示用
def put_count(screen, sel_count, swap_count):
    # フォントの生成
    font = pygame.font.Font(None, 40)
    # 前のスコアは黒で塗りつぶす
    block_img = get_block_img(0)
    screen.blit(block_img, (220 , 580))
    screen.blit(block_img, (500 , 580))

    score_img = font.render(str(sel_count), True, (255, 255, 0))
    screen.blit(score_img, (220, 580))

    score_img = font.render(str(swap_count), True, (255, 255, 0))
    screen.blit(score_img, (500, 580))
    # 画面を更新
    pygame.display.update()


# 選択対象をセット
def set_selection(sel_arr, t):
    for i in range(0, len(sel_arr)):
        if i == t:
            sel_arr[i] = -1
        else:
            sel_arr[i] = 0


# 選択ソート
def selectionSort(screen, sort_arr, sel_arr, sort_speed):
    # パラメータの配列の長さ
    n = len(sort_arr)
    sel_count = 0
    swap_count = 0

    # パラメータの配列の長さ-1回ループする（最後の1つは自然に決まるので-1）
    for i in range(n - 1):

        # iの要素以降で一番小さい数のindexを選択し、iと入れ替える
        sel_count += 1
        num = sort_arr[i:].index(min(sort_arr[i:]))
        # 比較対象をセット
        set_selection(sel_arr, num + i)

        # 盤面の更新
        put_frame(screen, sort_arr, sel_arr)
        put_count(screen, sel_count, swap_count)

        # 速度調整のsleep
        time.sleep(sort_speed)

        print(str(i) + "以降で一番小さい数は" + str(sort_arr[i + num]) + "で、")
        sort_arr[i], sort_arr[i + num] = sort_arr[i + num], sort_arr[i]
        print("入れ替えると" + str(sort_arr) + "になります")
        swap_count += 1

        # 盤面の更新
        put_frame(screen, sort_arr, sel_arr)
        put_count(screen, sel_count, swap_count)

        # 速度調整のsleep
        time.sleep(sort_speed)


# インポートされた時にプログラムが動かないように
if __name__ == "__main__":
    # 実行！
    main()

import numpy as np
import cv2
import sys
import os
import shutil
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton)


#指定されたディレクトリの中のファイルを全削除
def delete_files(directry):
    file_names = os.listdir(directry)
    for file_name in file_names:
        if file_name == ".gitkeep":
            continue
        os.remove(directry+file_name)

#画像をリサイズ
def resize(img, base_w, base_h):
    base_ratio = base_w / base_h   #リサイズ画像サイズ縦横比
    img_h, img_w = img.shape[:2]   #画像サイズ
    img_ratio = img_w / img_h      #画像サイズ縦横比

    white_img = np.zeros((base_h, base_w, 3), np.uint8) #白塗り画像のベース作成
    white_img[:,:] = [255, 255, 255]                    #白塗り

    ###画像リサイズ, 白塗りにオーバーレイ
    if img_ratio > base_ratio:
        h = int(base_w/img_ratio)           #横から縦を計算
        w = base_w                          #横を合わせる
        resize_img = cv2.resize(img, (w,h)) #リサイズ
    else:
        h = base_h                          #縦を合わせる
        w = int(base_h*img_ratio)           #縦から横を計算
        resize_img = cv2.resize(img, (w,h)) #リサイズ

    white_img[int(base_h/2-h/2):int(base_h/2+h/2),int(base_w/2-w/2):int(base_w/2+w/2)] = resize_img #オーバーレイ
    resize_img = white_img #上書き

    return resize_img

#dataフォルダ内の画像を連続リサイズ
def main(base_w, base_h):
    delete_files("./result/") #resultに入っている全ファイルを削除

    #dataディレクトリの画像を読み込み，リサイズ，resultディレクトリに保存
    file_names = os.listdir("./data/")
    for file_name in file_names:
        if file_name == ".gitkeep":
            continue
        print(file_name)

        #名前を変更した一時ファイルを保存(日本語名の画像をOpenCVが読み込めないため)，画像読み込み
        root, ext = os.path.splitext(file_name)
        read_tmp = "./tmp" + ext
        shutil.copyfile("./data/"+file_name, read_tmp)
        img = cv2.imread(read_tmp)
        os.remove(read_tmp)

        #リサイズ
        resize_img = resize(img, base_w, base_h)

        #名前を変更した画像を書き込み(日本語名の画像をOpenCVが書き込めないため)，リネーム
        write_tmp = "./result/tmp.jpg"
        cv2.imwrite(write_tmp, resize_img)
        os.rename(write_tmp, "./result/"+root+".jpg")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("usage: python resize.py width height")
        sys.exit(0)
    main(int(sys.argv[1]), int(sys.argv[2]))

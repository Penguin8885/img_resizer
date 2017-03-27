import numpy as np
import cv2
import os
import shutil

if __name__ == '__main__':
    file_names = os.listdir("./result/")
    for file_name in file_names:
        os.remove("./result/"+file_name)

    file_names = os.listdir("./data/")
    for file_name in file_names:
        print(file_name)

        #名前を変更した一時ファイルを保存(日本語名の画像をOpenCVが読み込めないため)，画像読み込み
        root, ext = os.path.splitext(file_name)
        read_tmp = "./tmp" + ext
        shutil.copyfile("./data/"+file_name, read_tmp)
        img = cv2.imread(read_tmp)
        os.remove(read_tmp)

        #リサイズ
        resize_img = cv2.resize(img, (280, 200))

        #名前を変更した画像を書き込み(日本語名の画像をOpenCVが書き込めないため)，リネーム
        write_tmp = "./result/tmp.jpg"
        cv2.imwrite(write_tmp, resize_img)
        os.rename(write_tmp, "./result/"+root+".jpg")

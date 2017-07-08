# プログラムについて
 画像をアスペクト比を変えずにリサイズします．  
 余白は白で塗りつぶされます．JPEG画像に変換されます  

# 環境
 Python, OpenCVが必要  
 (GUIを使うときはPyQtが必要)  

# 使い方
 resize.pyがあるディレクトリにinput, outputというフォルダを作っておきます．  
 inputフォルダにリサイズしたい画像を入れます．実行後にoutputにリサイズされた画像が保存されます．

 **[注意]** 実行時の初期化によって，outputフォルダの中身は全消去されます．

## resize.pyの使い方
 次のようにコンソールから実行します．<br>
 `python resize.py 280 200`<br>
 この例では，inputフォルダの画像がすべて横280，縦200の画像にリサイズされます．<br>

## resize_gui.pyの使い方
 次のようにコンソールから実行します．<br>
 `python resize.py`<br>
 weight, heightにリサイズする横と縦のサイズを入力してstartボタンを押すと，inputフォルダの画像がすべて指定の横と縦サイズの画像にリサイズされます．<br>
 <img src="https://github.com/Penguin8885/img_resizer/blob/master/sample_image/gui_sample_image.png" alt="GUIサンプル画像" title="GUIサンプル画像">
 
# サンプル画像
 ## input
 200, 200の画像
 <img src="https://github.com/Penguin8885/img_resizer/blob/master/sample_image/input_sample_image.jpg" alt="inputサンプル画像" title="inputサンプル画像">
 
 ## output
 500, 800でリサイズした結果<br>
 元画像の縦横比と違うので上と下に白い部分ができている
 
 <img src="https://github.com/Penguin8885/img_resizer/blob/master/sample_image/output_sample_image.jpg" alt="outputサンプル画像" title="outputサンプル画像">

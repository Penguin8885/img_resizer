import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit, QPushButton)
import resize

class Logger(object):
    def __init__(self, editor, out):
        self.editor = editor    # 結果出力用のエディター
        self.out = out          # 標準出力・標準エラーなどの出力オブジェクト

    def write(self, message):
        self.editor.insertPlainText(message)    #エディターにメッセージを書き出す
        self.out.write(message)                 #標準出力などにもメッセージを書き出す

    def flush(self):
        pass

#メインウィンドウのクラス
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        ##入力フォーム，ボタンの生成
        self.inputWidthLine = QLineEdit()               #横幅入力フォーム
        self.inputHeightLine = QLineEdit()              #縦幅入力フォーム
        self.startButton = QPushButton("&Start")        #スタートボタン
        self.startButton.clicked.connect(self.start)    #スタートボタンを押したときにする処理を設定
        self.logText = QTextEdit()                      #ログ表示用テキストボックス
        self.logText.setReadOnly(True)                  #読み取り専用に設定
        self.logText.setUndoRedoEnabled(False)          #Undo, Redo使用不可に設定
        sys.stdout = Logger(self.logText, sys.stdout)

        ##レイアウトを設定
        inputLineLayout = QGridLayout()                         #グリッドレイアウト
        inputLineLayout.addWidget(QLabel("width"), 0, 0)        #(0,0)にwidthラベルを配置
        inputLineLayout.addWidget(self.inputWidthLine, 0, 1)    #(0,1)に横幅入力フォームを配置
        inputLineLayout.addWidget(QLabel("height"), 1, 0)       #(1,0)にheightラベルを配置
        inputLineLayout.addWidget(self.inputHeightLine, 1, 1)   #(1,1)に縦幅入力フォームを配置
        buttonLayout = QVBoxLayout()                            #垂直ボックスレイアウト
        buttonLayout.addWidget(self.startButton)                #スタートボタンを配置
        mainLayout = QVBoxLayout()                              #水平ボックスレイアウト
        mainLayout.addLayout(inputLineLayout)                   #入力フォーム系を配置
        mainLayout.addLayout(buttonLayout)                      #スタートボタン系を配置
        mainLayout.addWidget(self.logText)

        ##ウィンドウに配置
        self.setLayout(mainLayout)

        ##ウィンドウスタイルを設定
        self.setGeometry(300, 300, 250, 200)
        self.setWindowTitle('resize')
        self.show()

    def start(self):
        width = int(self.inputWidthLine.text())
        height = int(self.inputHeightLine.text())
        resize.main(width, height)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())

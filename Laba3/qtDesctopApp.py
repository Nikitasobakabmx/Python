import sys
import socket
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
class Example(QWidget):
    host = None
    port = None
    sock = None
    textEdit = None
    textPecive = None
    def __init__(self, host = "127.0.0.1", port = 27015, massage = None):
        super().__init__()
        #
        self.host = host
        self.port = port
        self.sockInit()
        if(massage != None):
            self.reception()
            self.transmit(massage)
        #
        self.init_ui()

    def reception(self):
        result = self.sock.recv(1024)
        return result.decode('utf8')
    
    def sockInit(self):
        if self.host == None:
            return
        if self.port == None:
            return
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.host, self.port))

    def init_ui(self):
        layout = QVBoxLayout()
        label = QLabel("Insert name of file, then text")
        layout.addWidget(label)
        
        self.resize(300, 500)
        self.setWindowTitle("App")

        hLayout = QHBoxLayout()


        self.textEdit = QTextEdit()
        self.textEdit.resize(250,400)
        hLayout.addWidget(self.textEdit)

        self.textPecive = QTextEdit()
        hLayout.addWidget(self.textPecive)

        layout.addLayout(hLayout)

        secHLayout = QHBoxLayout()

        sendButton = QPushButton("Send")
        secHLayout.addWidget(sendButton)
        sendButton.released.connect(self.serverSend)

        button = QPushButton("Press me")
        secHLayout.addWidget(button)
        layout.addLayout(secHLayout)
        button.released.connect(self.write_to_file)

        self.setLayout(layout)
        self.show()

    def serverSend(self):
        if self.textEdit == None:
            return
        if self.textPecive == None:
            return
        self.textPecive.clear()
        massage = self.reception()
        self.textPecive.setText(massage)
        massage = self.textEdit.toPlainText()
        self.textEdit.clear()
        self.transmit(massage)

    def transmit(self, massage):
        self.sock.send(massage.encode('utf8'))

    def write_to_file(self):
        global textEdit
        if textEdit == None:
            return
        string = textEdit.toPlainText()
        stringList = string.split("\n")
        tmp = True
        for string in stringList:
            if tmp:
                tmp = False
                file = open(string,"w")
            else:
                file.write(string + "\n")
        textEdit.clear()
        
def main():
    app = QApplication(sys.argv)
    if len(sys.argv) == 4:
        host = str(sys.argv[1])
        port = int(sys.argv[2])
        massage = sys.argv[3]
        ex = Example(host, port, massage)
    else:
        ex = Example()
    sys.exit(app.exec_())
main()
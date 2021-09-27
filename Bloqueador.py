import sys
from EncryptPDF import EncryptPDF

if __name__ == '__main__':
    if sys.argv.count == 0:
        exit
    
    encrypt = EncryptPDF()
    senha   = sys.argv[sys.argv.index('-S') + 1]
    caminho = sys.argv[sys.argv.index('-D') + 1]
    encrypt.Criptografa(caminho, senha)
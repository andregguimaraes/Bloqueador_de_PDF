import sys
from EncryptPDF import EncryptPDF

if __name__ == '__main__':
    if sys.argv.count == 0:
        exit
    print("Iniciando processo...")
    
    encrypt = EncryptPDF()
    senha = sys.argv[sys.argv.index('-S') + 1]
    caminho = sys.argv[sys.argv.index('-C') + 1]

    encrypt.Criptografa(caminho, senha)
    print("Processo concluído, verifique o arquivo de Log para detalhes...")
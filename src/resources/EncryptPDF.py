import PyPDF2
import sys

class EncryptPDF():

    def __init__(self):
        pass

    def Criptografa(self, caminho_pdf: str, senha: str) -> bool:
        try:
            print('Iniciando processo...')
            arquivo_pdf = open(caminho_pdf, 'rb')
            caminho_pdf_criptografado: str = caminho_pdf.replace(
                '.pdf', '_criptografado.pdf')
            
            inputpdf = PyPDF2.PdfFileReader(arquivo_pdf)
            
            numero_paginas = inputpdf.numPages
            
            outputStream = open(caminho_pdf_criptografado, "wb")
            
            output = PyPDF2.PdfFileWriter()

            for i in range(numero_paginas):
                output.addPage(inputpdf.getPage(i))
                
            output.encrypt(senha)
            output.write(outputStream)
        except Exception as e:
            print('Ocorreu um erro ao tentar criptografar o arquivo com senha.')
            print(e)
            sys.exit(1)
        finally:
            arquivo_pdf.close()
            outputStream.close()
            print('Processo concluído com sucesso.')
            sys.exit(0)

import PyPDF2
import logging
import os
from datetime import datetime


class EncryptPDF():

    def __init__(self):
        pass

    def Criptografa(self, caminho_pdf: str, senha: str) -> bool:
        pasta_log = os.path.dirname(caminho_pdf)
        hora = datetime.today().strftime('%H%M%S')
        pasta = pasta_log + "\\" + 'LOG'
        if not os.path.exists(pasta):
            os.mkdir(pasta)
        pasta_log = os.path.join(pasta, 'log{}.csv'.format(
            ''.join(c for c in hora if c.isdigit())))
        open(pasta_log, "x")

        logging.basicConfig(filename=pasta_log,
                            encoding='utf-8', level='INFO')

        logging.info('Iniciando o processo...')

        try:
            arquivo_pdf = open(caminho_pdf, 'rb')
            caminho_pdf_criptografado: str = caminho_pdf.replace(
                '.pdf', '_criptografado.pdf')
            inputpdf = PyPDF2.PdfFileReader(arquivo_pdf)
            numero_paginas = inputpdf.numPages
            outputStream = open(caminho_pdf_criptografado, "wb")
            output = PyPDF2.PdfFileWriter()

            for i in range(numero_paginas):
                output.addPage(inputpdf.getPage(i))
                logging.info('Escrevendo novo arquivo, página ' + str(i))

            output.encrypt(senha)
            output.write(outputStream)
        except Exception as e:
            logging.error(
                'Ocorreu um erro ao tentar criptografar o arquivo, consulte o log para mais informações')
            logging.error(e)
        finally:
            arquivo_pdf.close()
            outputStream.close()
            logging.info('Novo arquivo salvo no diretório:' +
                         caminho_pdf_criptografado)

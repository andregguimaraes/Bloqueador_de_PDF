# Bloqueador_de_PDF

Utilitário para criptografia de PDFs por meio de senha.


## Documentação

### Montando Ambiente de Desenvolvimento

1. Instale o Python para Windows (ou Linux), e uma IDE de sua preferência (sugestão: VSCode, com a extenção "Python" da própria Microsoft) O script de execução do projeto é bloqueador.py. Basta executar com F5. É possível utilizar breakpoints
3. Clone o repositório localmente
2. Instale a extensão PyPdf2 via CMD.
	>Python -m pip install PyPdf2
6. Configure o arquivo launch.json que é gerado pelo vsCode, com o objetivo de passar parâmetros para o script em tempo de execução. O script foi desenvolvido para receber parametros com o prefixo -S (Senha) e -D (Diretorio).

### Executando o Bloqueador
Para rodar o bloqueador em seu ambiente de desenvolvimento, após configurar o arquivo launch.json conforme citado acima, basta rodar o seguinte comando:

> python <repositorio_dir>pdf_encrypt/bloqueador.py


### Gerando o executável
O Bloqueador de PDF utiliza a extensão PyInstaller para gerar executáveis no Windows. O programa pode ser gerado através do "Build.bat" localizado na pasta raiz do projeto. Caso encontre qualquer inconsistência durante a execução verifique se as instalações do Python e PyInstaller foram feitas corretamente, além do PATH contido nas variáveis de ambiente.

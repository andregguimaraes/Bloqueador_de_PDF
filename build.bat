@SET PYTHONPATH=%CD%\src
@SET BUILDPATH=%CD%\build
@SET PARAMS=-y --clean^
 --onefile^
 -p %PYTHONPATH%^
 --name "Bloqueador"^
 --distpath "%BUILDPATH%"^
 --workpath "%BUILDPATH%"

@SET PARAMS64=-y --clean^
 --onefile^
 -p %PYTHONPATH%^
 --name "Bloqueador64"^
 --distpath "%BUILDPATH%"^
 --workpath "%BUILDPATH%"


@IF EXIST venv (
  @CALL @%CD%\venv\Scripts\deactivate.bat
)

@IF EXIST venv64 (
  @CALL @%CD%\venv64\Scripts\deactivate.bat
)

@ECHO ##### Criando o ambiente virtual em 32 bits#####

@python -m venv --clear venv

@ECHO ##### Compilando o projeto em 32 bits #####

@CMD "/c @%CD%\venv\Scripts\activate.bat && @pip install -r requirements.txt && @pyinstaller %PARAMS% src\main\Bloqueador.py && @%CD%\venv\Scripts\deactivate.bat"


@ECHO ##### Criando o ambiente virtual em 64 bits#####

@"C:\Python37-64\python.exe" -m venv --clear venv64

@ECHO ##### Compilando o projeto em 64 bits #####

@CMD "/c @%CD%\venv\Scripts\activate.bat && @pip install -r requirements.txt && @pyinstaller %PARAMS64% src\main\Bloqueador.py && @%CD%\venv64\Scripts\deactivate.bat"

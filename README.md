Troca do Bem
===================

Repositório referente a aplicação web Troca do bem

----------

Requerimentos para executar o Troca do Bem
-------------
> **Passos**

> - Clone o projeto (necessário ter o pip instalado na maquina, python 2.7):

        git clone https://github.com/tainahemmanuele/trocadobem.git

> - Após clonar, entre na pasta do projeto , e execute:

        pip install -r requirements.txt 


Configurando o ambiente de testes
-------------
> **Passos**

> - Fazer download desta versao do Firefox: https://ftp.mozilla.org/pub/firefox/releases/46.0.1/win64/en-US/
> - Instalar o Firefox.
> - No Firefox, baixar a extension Selenium IDE (addons): https://addons.mozilla.org/en-US/firefox/addon/selenium-ide/?src=search
> - Gravar os testes montando suítes, dentro do proprio Selenium, ao terminar, exportar com python 2.7 (webdriver local - 1° opção python) dentro da pasta de tests.
> - Para rodar o teste individualmente, faça:

         python manage.py test app.tests.<nome-do-test-sem-.py-no-final>

> - Para rodar todos os testes e verificar as violações no código (quality), faça:

         ./runTests.sh 

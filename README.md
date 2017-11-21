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

Executando o projeto
-------------
> **Execute no terminal:**

         python manage.py makemigrations
         python manage.py migrate
         python manage.py runserver

> - Por fim,acesse: http://localhost:8000/

Regras para implementação (commit, push, pull)
-------------

> **Criando a branch para desenvolver:**

> - Acesse o tuleap-campus, e observe o número da sua task (ex. Task #19152)

> - Crie uma nova branch com nome task_numero_da_task (sem hashtag, tudo minusculo):

      git checkout -b <nome_da_branch> 

> - Nessa sua branch faça seus commits e aletrações necessárias.

> **Enviando suas alterações para o git:**
> - No terminal, execute:

        git add .

        git commit -am "Mensagem do commit"

        git checkout master

        git pull origin master

        git checkout <nome_da_sua_branch>

        git merge master

        git push origin <nome_da_sua_branch>

Verifique se foi feito o pull request.Caso não tenha sido enviado via terminal, solicite via interface gráfica.Depois, basta esperar a  revisão e aprovação do código.


Regras para revisão (Procedimentos que os revisores devem seguir)
-------------
> - ir para a branch que está em pull request.
> -  executar em um terminal: 

        ./manage.py migrate
        ./manage.py runserver 
        
> - rodar em outro terminal

        ./runTests.sh
        
> - pylint deve ser menor ou igual que 5
> - flake8 deve ser menor ou igual que 69
> - Todos os testes devem passar.
> - ao analisar o código verificar se os arquivos modificados possuem o cabeçalho:

      """<Nome-do-arquivo>.py: Descricao do arquivo aqui."""

          __author__ = "Author do Arquivo"
          __copyright__ = "Copyright 2017, LES-UFCG"

> - Verificar se os arquivos modificados possuem uma linha no fim do arquivo.
> - Funções devem NÂO devem ser camelCase, e sim tudo minusculo, separado por hifen (ex: def minha_function(): )
> - As Classes e funções devem estar todas documentadas.
> - Por fim, verificar se a implementação realiza o que está sendo pedido no requisito.
> - IMPORTANTE: AO APROVAR O CODIGO, É OBRIGATORIO ANEXAR UMA IMAGEM/PRINT/ESCRITO DO CONSOLE/TERMINAL MOSTRANDO OS VALORES DE PYLINT E FLAKE8


Versão em produção do Troca do Bem:
-------------

Versão mais estável do sistema:

https://trocadobem.herokuapp.com/

# PT / EN


## API: Monitorização de Tráfego Rodoviário
Este projeto foi desenvolvido como parte de um exercício técnico num processo de recrutamento. O objetivo principal é criar uma REST API usando o Django Rest Framework que permita ser usado como uma *dashboard* para monitorizar o tráfego rodoviário e permitir uma melhor análise do utilizador quanto ao fluxo de tráfego que existe num determinado troço.

## Funcionalidades
- **Lista dos Segmentos de Estrada:** Permite visualizar todos os segmentos de estrada na database - como os dados geográficos, velocidade média e data e hora de registo.
- **Detalhes do Segmento de Estrada:** É possível obter os detalhes de um ou mais segmentos de estrada com base nos filtros implementados (através do ID, velocidade e/ou intensidade de tráfego).
- **Permissões do Administrador:** Adicionar, editar e remover qualquer segmento de estrada. O administrador também consegue visualizar os segmentos de estrada mais procurados, pelo usuário comum - anónimo.
- **Gestão de Utilizadores:** Através de django-admin permite fazer uma gestão dos utilizadores autenticados (e.g. outros administardores).

## Requisitos
Para poder executar este projeto API, foram usados:
```
python==3.12.5 #Python version
Django==5.1 #Django version
djangorestframework==3.15.2 #Django Rest Framework version
psycopg2==3.2.1 #psycopg2 version
drf-yasg==1.21.7 #Swagger API version
django-leaflet==0.30.1 #Leaflet version
```

## Início do Projeto

### Clonar o repositório
```
git clone https://github.com/AfonsoAvila/API_Monitor_Trafego
```

### Diretório
Ao entrar no diretório onde foi clonado o repositório, deve ativar o ambiente virtual
```
venv\Scripts\activate
```
Ou poderá fazê-lo manualmente no VSCode, no menu "View" e em "Command Palette", exolhendo o "Python Interpreter" e o correspondente ambiente virtual.

### Instalação dos requisitos
Correr o comando:
```
pip install -r requirements.txt
```

### Migrar a base de dados e data inicial
Deve migrar a base de dados e dizer onde ir buscar a data inicial. Para isso, corra os comandos:
```
python manage.py makemigrations
python manage.py migrate
```
E após criadas as migrações, corra o comando para popular a base de dados:
```
python manage.py load_trafego_dataset
```
Este comando ira correr o código que extrai a base de dados providenciada no repositório github fornecido.

### Começar o servidor
Neste momento, deverá ser possível executar o servidor correndo o comando:
```
python manage.py runserver
```

## Usar a API

Ao iniciar o servidor, a primeira página local (http://127.0.0.1:8000/ ou localhost:8000) mostrará uma página criada em .html (na pasta templates) com todas as opções possíveis ao utilizador. Então, para se autenticar como administrador, terá de clicar no **"Admin Dashboard"** e iniciar a sessão usando *admin_visit* como usuário e *admin_password* como senha.
Os Endpoints possíveis estão percetíveis.

## Testar a API
Foram criados 10 testes unitários na API. Pode testar a API com o comando:
```
python manage.py test
```

## Informações

Para mais informações ou algum problema, poderá contactar-me no e-mail: afonso.avila2001@gmail.com




##----------------------------------------EN----------------------------------------------##



## API: Traffic Monitoring
This project was developed as part of a technical exercise in a recruitment process. The main objective is to create a REST API using the Django Rest Framework that can be used as a dashboard to monitor road traffic and allow better user analysis of the traffic flow on a given section of road.

## Features:
- **List of Road Segments:** This allows you to view all road segments in the database, including geographic data, average speed, and registration date and time.
- **Road Segment Details:** Based on the implemented filters (through ID, speed, and/or traffic intensity), it is possible to obtain details of one or more road segments.
- **Administrator Permissions:** Add, edit and remove any road segment. The administrator can also view the most popular road segments by the common user - anonymous.
- **User Management:** Using django-admin allows you to manage authenticated users (e.g. other administrators).

## Requirements
To be able to run this API project, it was used:
```
python==3.12.5 #Python version
Django==5.1 #Django version
djangorestframework==3.15.2 #Django Rest Framework version
psycopg2==3.2.1 #psycopg2 version
drf-yasg==1.21.7 #Swagger API version
django-leaflet==0.30.1 #Leaflet version
```

## Project Start

### Clone the repository
```
git clone https://github.com/AfonsoAvila/API_Monitor_Trafego
```

### Directory
When entering the directory where the repository was cloned, you must activate the virtual environment
```
venv\Scripts\activate
```
You can do it manually in VSCode, in the “View” menu and in “Command Palette”, removing the “Python Interpreter” and the corresponding virtual environment.

### Installation of requirements
Run the command:
```
pip install -r requirements.txt
```

### Migrate the database and initial data
It must migrate the database and tell it where to get the initial data. To do this, run the commands:
```
python manager.py migrations
python manager.py migrate
```
And after the migrations are created, run the command to populate the database:
```
python manager.py load_trafego_dataset
```
This command will run the code that pulls from the provided database in the provided github repository.

### Start the server
At this point, it should be possible to run the server by running the command:
```
python manager.py run server
```

## Use an API

When starting the server, the first local page (http://127.0.0.1:8000/ or localhost:8000) will show a page created in .html (in the templates folder) with all the possible options for the user. So, to authenticate as an administrator, you will have to click on the **"Admin Dashboard"** and log in using *admin_visit* as username and *admin_password* as password.
Possible Endpoints are noticeable.

## Test an API
10 unit tests were created on the API. You can test an API with the command:
```
python test manage.py
```

## Information

For more information or any problems, you can contact me at: afonso.avila2001@gmail.com

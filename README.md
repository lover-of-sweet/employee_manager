# employee_manager

## 1. Запуск программы при помощи _docker_
- Склонировать репозиторий с кодом или скачать код с репозитория <br/>
- Запустить _docker-compose_ командой docker compose up <br/>
- После запуска необходимо перейти по адресу _http://127.0.0.1:8000/manager/positions_<br/>

## 2. Запуск программы не с _docker_
- Склонировать репозиторий с кодом или скачать код с репозитория <br/>
- Перейти в файл employee_management/employee_management/settings.py и в переменной DATABASES расскоментировать строку 
'HOST': 'localhost', и закомментировать строку 'HOST': 'db' <br/>
- БД рекомендуется разворачивать при помощи _docker_<br/>
- Все sql скрипты для создания и первичного наполнения находся в init.sql<br/>
- После развоваричания БД, необходимо запустить файл employee_management/manage.py командой
`python3 manage.py runserver`<br/>
- После запуска необходимо перейти по адресу _http://127.0.0.1:8000/manager/positions/_<br/>

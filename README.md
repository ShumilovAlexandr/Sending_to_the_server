# Описание
Проект реализован с помощью языка программирования Python версии 3.10.2, фреймворка Django, а
также с помощью иснтрумента создания веб-интерфейсов Django REST Framework
Проект **FabV** отвечает за отправку сообщений на внешний сервер

## Суть процесса рассылки сообщений
Так как внешний сервер, принимающий сообщения, может долго обрабатывать входящий запрос, либо некорректно
принять запрос, а также учитывая, что рассылка сообщений должна происходить в фоновом режиме,
в проекте реализована отправка сообщений с помощью очереди задач Celery

### Брокер
В качестве брокера очередей сообщений в проекте используется Reddis

#### Как запустить преокт:
1. Клонировать проект по ссылке https://github.com/ShumilovAlexandr/Sending_to_the_server
2. Создать и активировать виртуальное окружение командами python -m venv venv, . venv/bin/activate
3. Установить зависимости из файла requirements.txt: python -m pip install --upgrade pip,
pip install -r requirements.txt
4. Выполнить миграции: python manage.py migrate
5. Запустить проект python manage.py runserver
6. В отдельной вкладке запустить Celery: celery -A src worker -l info 
7. Не забыть забустить брокер очередей (я это делал через windows ubuntu): sudo service redis-server start

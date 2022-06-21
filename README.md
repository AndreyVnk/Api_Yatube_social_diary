# API Yatube

**Yatube** - это блог, в котором пользователи могут публиковать свои записи и фото.

**API Yatube** поддерживает обмен данными в формате *JSON*.

Система аутентификация реализована через получение JWT-токена. Функционал API предоставляет следующие ресурсы:

- Записи
- Комментарии
- Группы

Реализована возможность подписываться на других пользователей.

Развернув проект у себя, Вы можете ознакомиться с документацией к API по ссылке [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/).

* Python 3
* Django Rest Framework
* Simple JWT
* SQLite

## Запуск проекта ##
### 1. Склонировать репозиторий
```
git clone https://github.com/AndreyVnk/Api_Yatube_social_diary.git
```

### 2. Создать виртуальное окружение и активировать его
Перейти в папку с проектом _Api_Yatube_social_diary/_ выполнить команды
```
python -m venv venv
source venv/Scripts/activate (для Windows) | source venv/bin/activate (для Linux)
```
### 3. Создать в корневой папке проекта и заполнить файл _.env_
```
SECRET_KEY=secret_django_key
```
### 4. Установить необходимые пакеты
```
pip install -r requirements.txt
```
### 5. Выполнить миграции
Из папки *Api_Yatube_social_diary/yatube_api/*, выполнить команду
```
python manage.py migrate
```
### 6. Запустить проект
```
python manage.py runserver
```
Эндпоинты, описанные в документации доступны на корневом адресе проекта: http://127.0.0.1:8000/api/v1/ . Документация к API доступна на http://127.0.0.1:8000/redoc/ .

**Автор**

AndreyVnk

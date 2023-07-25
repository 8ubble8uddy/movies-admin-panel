## Movies Admin Panel

[![python](https://img.shields.io/static/v1?label=python&message=3.8%20|%203.9%20|%203.10&color=informational)](https://github.com/8ubble8uddy/movies-admin-panel/actions/workflows/main.yml)
[![dockerfile](https://img.shields.io/static/v1?label=dockerfile&message=published&color=2CB3E8)](https://hub.docker.com/r/8ubble8uddy/django_admin_panel)
[![last updated](https://img.shields.io/static/v1?label=last%20updated&message=july%202022&color=yellow)](https://img.shields.io/static/v1?label=last%20updated&message=july%202022&color=yellow)
[![lint](https://img.shields.io/static/v1?label=lint&message=flake8%20|%20mypy&color=brightgreen)](https://github.com/8ubble8uddy/movies-admin-panel/actions/workflows/main.yml)
[![code style](https://img.shields.io/static/v1?label=code%20style&message=WPS&color=orange)](https://wemake-python-styleguide.readthedocs.io/en/latest/)
[![tests](https://img.shields.io/static/v1?label=tests&message=%E2%9C%94%205%20|%20%E2%9C%98%200&color=critical)](https://github.com/8ubble8uddy/movies-admin-panel/actions/workflows/main.yml)

### **Описание**

_Целью данного проекта является реализация интерфейса администратора для загрузки фильмов и редактирования информации о них. В связи с этим была разработана административная панель на основе фреймворка [Django](https://www.djangoproject.com). В качестве базы данных используется [PostgreSQL](https://www.postgresql.org). Проект подготовлен к запуску в production-окружении через веб-сервер [NGINX](https://nginx.org). Для проверки результата работы API используется [Postman](https://www.postman.com)._

### **Технологии**

```Python``` ```Django``` ```PostgreSQL``` ```NGINX``` ```Gunicorn``` ```Postman``` ```Docker```

### **Как запустить проект:**

Клонировать репозиторий и перейти внутри него в директорию ```/infra```:
```
git clone https://github.com/8ubble8uddy/movies-admin-panel.git
```
```
cd movies-admin-panel/infra/
```

Создать файл .env и добавить настройки для проекта:
```
nano .env
```
```
# PostgreSQL
POSTGRES_DB=movies_database
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=postgres
POSTGRES_PORT=5432

# Django
DJANGO_SUPERUSER_USERNAME=admin
DJANGO_SUPERUSER_EMAIL=admin@mail.ru
DJANGO_SUPERUSER_PASSWORD=1234
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1,[::1],django
DJANGO_SECRET_KEY=django-insecure-_o)z83b+i@jfjzbof_jn9#%dw*5q2yy3r6zzq-3azof#(vkf!#
```

Развернуть и запустить проект в контейнерах:
```
docker-compose up
```

Перейти в админ-панель и ввести логин (admin) и пароль (1234):
```
http://127.0.0.1/admin
```

### Автор: Герман Сизов
### **Как запустить тесты:**

Клонировать репозиторий и перейти внутри него в директорию ```/tests```:
```
git clone https://github.com/8ubble8uddy/movies-admin-panel.git
```
```
cd movies-admin-panel/tests/
```

Создать файл .env и добавить настройки для тестов:
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
```

Развернуть и запустить тесты в контейнерах:
```
docker-compose up --build --exit-code-from tests
```

### Автор: Герман Сизов
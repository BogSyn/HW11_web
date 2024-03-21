# Домашнє завдання #11

<b> Запуск Docker-контейнер, щоб створити сервер PostgreSQL: </b>

    docker run --name contactbook -p 5432:5432 -e POSTGRES_PASSWORD=1111 -d postgres

<b> Запуск веб-сервера Uvicorn командою з директорії main.py: </b>

    uvicorn main:app --host localhost --port 8000 --reload

<b> Створення міграцій: </b>

    alembic revision --autogenerate -m 'Init'

<b>Для застосування міграції з отриманого файлу та створення таблиць наших моделей у БД виконаємо команду: </b>

    alembic upgrade head



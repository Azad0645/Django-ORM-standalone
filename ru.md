# Пульт охраны банка

Описание проекта:
- Пульт охраны — это внутренний репозиторий для сотрудников банка, позволяющий отслеживать их пропуска. 

## Как установить 

Создайте файл .env в корневой папке проекта и заполните его следующими переменными окружения:
- DB_ENGINE=Бэкенд для подключения к базе данных 
- DB_HOST=Адрес сервера базы данных
- DB_PORT=Порт для подключения к базе данных
- DB_NAME=Название базы данных
- DB_USER=Имя пользователя 
- DB_PASSWORD=Пароль пользователя 
- SECRET_KEY=Секретный ключ 

Установка зависимостей:
- Python 3 должен быть уже установлен.

```bash
pip install -r requirements.txt
```

Запустите скрипт:

```bash
python main.py
```

## Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).
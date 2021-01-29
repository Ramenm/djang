1. Устанавливаем виртуальное окружение
2. Качаем модули командой pip install -r requirements.txt
3. Через manage.py делаем и применяем миграции командами makemigrations, migrate
4. Запустить парсер python hnews/parser.py
5. Через manage.py запускаем сервер локально командой runserver 8000
6. Заходим в браузере на 127.0.0.1:8000/posts/

Возможные атрибуты для GET запросов:
```
limit       int >0 and <30,
offset              int >0,
order       str field_name
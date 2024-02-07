# Бэкенд-часть SPA веб-приложения "Образовательная платформа"

### Установка:
- Убедитесь, что у вас установлен python 3.11 или более новая версия<br>
- Убедитесь, что у вас установлен PostgreSQL и запущен локальный сервер для базы данных<br>
- Убедитесь, что у вас установлен Redis и запущен redis-сервер<br>
- Склонировать репозиторий<br>
- Создать и активировать виртуальное окружение```python -m venv ваша_папка_для_виртуального_окружения```<br>
- Установить зависимости командой ```pip install -r requirements.txt```<br>
- Создать вашу базу данных для работы с проектом ```CREATE DATABASE ваша_база_данных;```<br>
- Создать миграции через ```python manage.py makemigrations``` и применить их ```python manage.py migrate```<br>
- В файле .env.sample заполнить данные для работы с проектом и переименовать его в .env<br>
- Открыть командную строку и запустить ```python manage.py runserver```<br>
- Для запуска Celery открыть другой экземпляр командной строки и запустить ```celery -A config worker -l INFO -P eventlet```<br>
- Для запуска django-celery-beat открыть другой экземляр командной строки и
  запустить ```celery -A config beat -l INFO -S Django```<br>

- Кастомная команда для создания суперпользователя ```python manage.py csu```<br>

### Используемые технологии:

- DjangoRestFramework<br>
- Docs/ReDoc ```host://docs/``` ```host://redoc/```, работает авторизация по Bearer токену<br>
- Redis<br>
- Celery<br>
- Платёжная система Stripe, реализация через сессии<br>
- Пагинация для вывода списка курсов
- DjangoFilters для фильтрации списка платежей

### Логика работы системы:

- Зарегистрировать пользователя ```/users/register/```<br>
- Получить токен пользователя ```/users/token/```<br>
- Создать курс, создать уроки в курсе
- Можно создать подписку на другой курс
- Так как у каждого курса можно указать стоимость - реализована работа с платёжной системой stripe через сессии.

### Права доступа:

- Каждый пользователь имеет доступ только к своим курсам и урокам по механизму CRUD.<br>
- Подписка на курс позволяет отслеживать изменения курса(редактирование курса, редактирование урока в курсе или создание
  нового урока)
- Предусмотрен функционал модератора, роль которого можно создать и назначить в админитративной панеле
- Модератор может видеть все курсы и уроки, может редактировать, но не может создавать или удалять их. Закрыт доступ к
  подпискам.

### Эндпоинты:

- Пользователи:
  - Создание пользователя
  - Просмотр деталей профиля
  - Редактирование профиля
  - Получение токена
  - Обновление токена
- Курс:
  - Создание курса
  - Список курсов
  - Информация о курсе
  - Редактирование курса
  - Удаление курса
- Урок:
  - Создание урока
  - Список уроков в курсе
  - Информация о уроке
  - Редактирование урока
  - Удаление урока
- Подписка:
  - Создание подписки
  - Просмотр подписки
  - Удаление подписки
- Платёж:
  - Список платежей
  - Создание платежа
  - Информация о платеже
  - Удаление платежа
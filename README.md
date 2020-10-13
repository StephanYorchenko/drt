PSharing
----

Web-приложение, предназначенное специально для онлайн-показа презентаций.

В наше непростое время, как никогда важно иметь способ быстро и с минимальными затратами показать презентацию
К сожалению, большинство существующих решений предполагают стабильное и скоростное интернет-соединение, что
доступно не всем. 

PSharing - минимизирует логистические расходы, поскольку отказывается от показа демонстрации экрана в виде 
потокового видео, в пользу показа отдельных слайдов, с возможностью отлистать эти слайды назад, или посмотреть презентацию 
позже

Компоненты:
1. Компонент Презентация:
```Представляет собой клиент-серверное приложение```
- Клиент:
    ```Реализована с использованием стека технологий JavaScript+HTML+CSS```
    - Интерфейс администратора
        - Поле с текущим слайдом
        - Добавление/переключение слайдов
        - чат
    - Интерфейс пользователя:
        - чат
        - Поле с текущим слайдом
        - Интерфейс перелистывания на другой слайд
    - Отправка запросов пользователей (получить слайд/ отправить сообщение/ обновить страницу)
- Сервер:
    ```Технологии: Python3, Flask, SQLAlchemy, PostgreSQL```
    - Обработка запросов пользователей (получить слайд/ отправить сообщение/ обновить страницу)
    - Проверка прав доступа
    - Взаимодействие с базой данных
        - Хранение данных учётных записей (логин/пароль)
        - Данные учебных классов (идентификатор)
        - Хранение слайдов
        - Отношение пользователей к классам (права доступа/пригашён ли в класс)
        - Отношение слайдов к паре (пользователь - класс)
2.  Компонент Администрирование:
```Клиент-серверное приложение```
- Клиент: ```Реализована с использованием стека технологий JavaScript+HTML+CSS```
    - Интерфейс Администрирование:
        - Изменение имени комнаты
        - Приглашение участников
        - Добавение слайдов
        - Настройка презентации
    - Отправка запросов пользователя на сервер
- Сервер: ```Технологии: Python3, Flask, SQLAlchemy, PostgreSQL```
    - Проверка прав доступа
    - Обработка пользовательских запросов
    - Валидация полученных данных из запроса. В случае подтверждения консистентости информации - применение изменений к существующей базе данных

3. Авторизация/регистрация
4. Главная страница:
    - Выбор комнаты
    - (для администратора) доступ к компоненту Администрирование для выбранной комнате

    

        - 
Ключевые особенности:
1. Показ слайдов ```Компонент Презентация```
    - [ ] В формате ppt/pptx (выложены зараннее)
    - [ ] pdf (выложены зараннее)
    - [x] jpg/png (выложены заранее)
    - [x] скрины экрана (динамически добавляются в процессе презентации)
2. Текстовый чат ```Компонент презентация```
    - [x] Общий текстовый чат
    - [ ] Голосовалки в чате
    - [ ] Отправка личных сообщений админу презентации
    - [x] Отправка png/jpg
    - [ ] Викторины в чате
3. Права доступа ```Компоненты Администрирование и Презентация```
    - [x] Публичные/приватные презентации
    - [x] Админ - может добавлять слайды/участников/менять права доступа
    - [ ] Модератор  - может удалять сообщения в чате/добавлять участников
    - [x] Участник - может писать в чат
    - [ ] Редактор - может менять презентацию
    - [ ] Премиум-аккаунт админа - снимает ограничение на количество хранимых презентаций


----
Состав команды разработки:
- Анчутин Никита
- Ложкин Александр
- Фролов Юрий
- Юрченко Степан

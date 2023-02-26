Для работы программы необходимо иметь установленную СУБД Postgresql По умолчанию настроено на следующие данные: DB_USER = "postgres" DB_NAME = "djan_p" DB_PASSWORD = "Vrt342zf" DB_HOST = "127.0.0.1" При использовании других учетных данных к БД, необходимо скорректировать в разделе "settings.py" Также необходимо наличие модулей из requirements.txt Программа запускается с помощью команды py  manage.py runserver  режиме сервера разработчика. После запуска необходимо перейти на http://127.0.0.1:8000/ где доступен список  маршрутов, 
основные admin/
data/
data_crt/
data_upd/<int:pk>
delete/<int:pk>
Например http://127.0.0.1:8000/admin/ вход в админ панель ресурса откуда можно управлять данными, для доступа необходимо создать пользователя командой   py  manage.py createsuperuser
Так же управление доступно с вышеперечисленных алиасов, стоит отметить что ссылки типа data_upd/int:pk, data_del/int:pk предполагают указание номера задачи int:pk для выполнения изменения или удаления конкретной задачи с определенным id.
Программа демонстрирует управление элементами модели данных из административной панели и из так же из браузера по вышеописанным ссылкам. Исходный код для удобочитаемости отформатирован посредством инструмента Black.

Дополнения от предыдущей реализации:
- реализовано API с помощью djangorestframework - дает управление из среды работающий с API
  - GET /api/zadachi - получть список всех задач
  - GET /api/zadachi/{id} - получть одну конкретную задачу
  - POST /api/zadachi - создать задачу
  - PUT (или PATCH) /api/zadachi/{id} - отредактировать существующую задачу
  - DELETE /api/zadachi/{id} - удалить одну задачу
- реализовано с пощью страничной пагинации  page отображение в 7 задач на странице
- реализовано использование фильтрации по задачам ?zadachi=... , ?ordering=..., активгости задачи active_switch=True/False
Пример url DRF http://127.0.0.1:8000/api/zadachis/53, где последнее число номер задачи и применимы вышеописанные методы, корректность ввода эндпоитов смотреть выше
Фильтрация http://127.0.0.1:8000/api/zadachis?.... , где после ? указывается способ фильтрации из описанных выше
Исходный код для удобочитаемости так же отформатирован посредством инструмента Black
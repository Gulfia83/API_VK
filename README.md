# Обрезка ссылок с помощью VK и подсчет кликов по короткой ссылке

Программа проверяет какая ссылка была задана на входе. Если ссылка длинная, то сокращает ее с помощью VK. По короткой ссылке подсчитывает количество кликов по ней.

### Как установить

Python3 должен быть установлен.
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```
Требуется получить сервисный ключ (токен) для взаимодействия с API VK. Для этого создайте приложение в [личном кабинете сервиса авторизации VK ID](https://id.vk.com/about/business/go/docs/ru/vkid/latest/vk-id/connection/create-application). Сохраните свой ключ в .env и введите его в main.py
```
token = os.environ['VK_API_KEY']
```
Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html)

### Пример запуска
```console
python main.py https://dvmn.org/modules/
https://vk.cc/aCA1ad
python main.py https://vk.cc/aCA1ad
По вашей ссылке перешли 3 раз
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе [dvmn.org](https://dvmn.org/)
# RoubleRankBot
Бот для получения курса рубля

Запуск бота локально:

1. Создадим пустого бота с помощью @BotFather - зададим ему имя и получим токен (ключ доступа)
2. Установим питоновскую библиотеку pytelegrambotapi, с удобной обёрткой для телеграма. Это можно сделать, например, с помощью пакетного менеджера pip. Все установленные библиотеки будем записывать в requirements.txt, чтобы потом они автоматически устанавливались на сервере.
3. Создадим файл main.py с примитивным ботом-повторюшкой. При запуске файла пароль от бота читается из переменных среды (чтобы не палить его в репозитории), создаются функции для ответа на сообщения, и бот запускается в режиме "polling" (когда ваша программа постоянно спрашивает Телеграм, нет ли обновлений)
4. Чтобы протестировать его, надо вписать пароль в переменные среды (вбить в командной строкеset TOKEN=... на винде или export TOKEN=... на маке и линуксе), а дальше запустить в командной строке python main.py (предварительно перейдя в с помощью cd в папку с кодом) - и бот заработает! P.S. Я тестировал это на python 3.6, но по идее всё должно работать и с другими версиями.

<h3 align="left">Connect with me:</h3>
<p align="left">
<a href="https://linkedin.com/in/vglnsk" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="vglnsk" height="30" width="40" /></a>
<a href="https://t.me/far_0011" target="_blank"><img align="center" src="https://img.shields.io/badge/-telegram-red?color=white&logo=telegram&logoColor=blue" alt="vglnsk" height="30"/></a>
</p>

### Технологии
    ```
    Python 3.9.10,
    pyTelegramBotAPI 4.14.1,
    Flask 3.0.0, 
    ```

### Автор
Антон Корчагин - [Far-001](https://github.com/Far-001)

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Python+developer+and+student)](https://git.io/typing-svg)
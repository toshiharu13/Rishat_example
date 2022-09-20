# Тестовое задание 
[![Python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)

## Описание
*Проект не закончен.*

Сайт с примитивными страницами предназанчен для демонстрации работы с платежной системой [сайт платёжной системы](https://stripe.com/)
После заполнения базы, на стартовой странице появляется список товаров, можно пройти на страницу каждого и , либо сделать покупку, либо вернуться обратно


## Как установить
 - Склонировать проект
```shell
git clone https://github.com/toshiharu13/Rishat_example.git
```
 - Установить requirements.txt
```shell
pip install -r requirements.txt
```
 - Создать файл .env и заполнить в нем переменные:
```dotenv
DEBUG= 'дебаг работы - True/False, False по умолчанию'
```
```dotenv
SECRET_KEY = 'секретный ключ, для DEV есть значение по умолчанию, для PROD обязательно заполнить'
```
```dotenv
ALLOWED_HOSTS = 'Адреса, которым разрешен доступ для запросов на сайт, по умолчанию есть localhost'
```
```dotenv
STRIPE_KEY = 'Ключ платёжноё системы для получения необходимо авторизоваться, или для DEV использовать тестовые ключи http://stripe.com/docs'
```
##Работа приостановлена, требуется изучить javascript и откорректировать запрос, ридерект на странице шаблона.
Что сделано: переход по страницам, запрос  в платёжную систему объекта сесии
Осталось: javascriptom запросить объект сессии и используя его данные выйти на чекаут форму

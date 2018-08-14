# Kiosk FLASK App

Проект простого Интернет-магазина "КИОСК"

## Описание

Проект отображает список товаров и их атрибутов и состоит из трех сущностей:
* Товары
* Атрибуты
* Значение атрибутов у товаров

, что схематично можно представить  ER-моделью (3NF) базы данных как
![KIOSK_ER_model](https://raw.githubusercontent.com/BorisPlus/otus_webpython_004/master/additional/docs/simple_ER_model.png "Title")


Если углубляться в реальные требования к подобному приложению, без реализации функционала
осуществления заказов пользователем, то не хватает многого (в т.ч. по БД), например:
* Отнесение товаров к категории
* Иерархия категорий
* Дополнительные изображения товара
* Учет типов атрибутов (целое, строка, период, множественный выбор, состоящий из других атрибутов атрибут) и их форматированный 
вывод пользователю
* Назначение товару группы аттрибутов и их значений
* Упорядочивание атрибутов и их групп у товаров
* Фильтрация товаров по атрибутам
* Еще много и много чего...
... но это выходит, как я понял, за рамки данного домашнего задания.


### Требования

Данный проект использует:
* Flask
* Flask-SQLAlchemy

Установите их

```python
pip3 install flask==0.10
pip3 install Flask-SQLAlchemy==2.3.2
```

или

```
pip3 install -r requirements.txt
```

### Использование

В качетве тестовой базы данных выбрана SQLite. 
Соответствующий файл с демонстрационными данными лежит в самом проекте **_kiosk/db/kiosk.db_**.

Чтобы запустить демонстрационный проект выполните
```bash
python3 /<absolute_path>/kiosk/app.py
```
чтобы очистить базу данных, можно просто удалить файл **_kiosk/db/kiosk.db_** и перезапустить приложение
или же выполнить 

```bash
python3 /<absolute_path>/kiosk/__init__.py
```
С целью демонстрации функционирования Веб-приложения "КИОСК" были разработаны модули получения данных
из Интернет-магазина "Мвидео" и их импорта в базу данных Веб-приложения "КИОСК". 
Модуль импорта задействует теже модели, что и само Веб-приложение. При реализации импорта с других 
ресурсов вы избавлены от написания SQL-инструкций на SELECT\INSERT, главное придерживаться 
формирования определенной структуры специального вида. Если Вам интересно, то ознакомтесь с  
[дополнительной документацией](https://github.com/BorisPlus/otus_webpython_004/tree/master/additional/ADDITIONAL_REPORT.md)
данного проекта.

При демонстрационном запуске с существующей проектной заполненной базой данных необходим доступ к сети Интернет,
так как ссылки на изображения товаров указывают на их реальные. Изображения не скачаны локально в проект.


## Авторы

* **BorisPlus** - [https://github.com/BorisPlus/otus_webpython_004](https://github.com/BorisPlus/otus_webpython_004)

## Лицензия

Распространяется свободно.

## Дополнительные сведения

Проект в рамках трехдневного домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning

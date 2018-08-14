# Демонстрационный вариант реализации импорта данных с ресурсов сети Интернет

С целью демонстрации функционирования Веб-приложения "КИОСК" были разработаны модули получения данных
из Интернет-магазина "Мвидео" и их импорта в базу данных Веб-приложения "КИОСК". 
Модуль импорта задействует те же модели, что и само Веб-приложение. При реализации импорта с других 
ресурсов вы избавлены от написания SQL-инструкций на SELECT\INSERT, главное придерживаться 
формирования структуры данных специального вида (рассмотрена ниже).


## Для разработчика

Папка **_additional/import_to_db_from/core_** содержит модуль, реализующий импорт данных
 в БД о товарах и их атрибутах. На вход функции _do_import_products_info_to_database_ 
 подается списочно-словарная структура специального вида.
 
 Ее вид можно описать примерно так:
 ```python
[
    {
        'main_image_path': STRING,
        'name': STRING,
        'description': STRING,
        'shop_url': STRING,
        'attrs': [
            {
                'name': STRING,
                'value': STRING,
            },
            {
                'name': STRING,
                'value': STRING,
            },
            ...
        ]
    },
    ...
]
```
### Пример тестовых данных

[Пример](https://github.com/BorisPlus/otus_webpython_004/tree/master/additional/import_to_db_from/data/test_data.py) 
заранее подготовленных данных лежит в **_additional/import_to_db_from/data/test_data.py_**, 
это данные с "Яндекс.Маркет", внесенные в указанную структуру вручную.

### Пример сбора данных с "Мвидео"

[Пример](https://github.com/BorisPlus/otus_webpython_004/tree/master/additional/import_to_db_from/data/mvideo_ru_data.py) 
сбора данных со страницы Интернет-магазина "Мвидео" - **_additional/import_to_db_from/data/mvideo_ru_data.py_**
Данный пример осуществляет разбор html-структуры страницы и выбирает значения, соответствущие полям 
товаров и атрибутов, приводя собираемые даные к вышеописанному специальному виду.

Пример использует библиотеки:
* beautifulsoup4=4.3.2
* urllib3=1.22

Установите их

```python
pip3 install beautifulsoup4==4.3.2
pip3 install urllib3==1.22
```

или

```
pip3 install -r requirements.txt
```
### Пример сбора данных и их импорта

[Демонстрационный пример](https://github.com/BorisPlus/otus_webpython_004/tree/master/additional/import_to_db_from/do_import.py) 
 сбора данных и их импорта в БД приведен в скрипте **_additional/import_to_db_from/do_import.py_**

```python
from additional.import_to_db_from.core.importer import do_import_products_info_to_database
from additional.import_to_db_from.data.mvideo_ru_data import get_products_info as get_mvideo_ru_products_info

if __name__ == '__main__':
    # сбор с первых 9 страниц о ноутбуках
    for i in range(2, 10):
        url = 'https://www.mvideo.ru/noutbuki-planshety-komputery/noutbuki-118/f/page=%s' % i
        do_import_products_info_to_database(get_mvideo_ru_products_info(url))
```

## Авторы

* **BorisPlus** - [https://github.com/BorisPlus/otus_webpython_004](https://github.com/BorisPlus/otus_webpython_004)

## Лицензия

Распространяется свободно.

## Дополнительные сведения

Проект в рамках трехдневного домашнего задания курса "Web-разработчик на Python" на https://otus.ru/learning

import os
import sys

kiosk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if kiosk_path not in sys.path:
    sys.path.append(kiosk_path)

from kiosk.config import db, db_path
from kiosk import models

if __name__ == '__main__':
    if os.path.exists(db_path):
        os.remove(db_path)
    db.create_all()

    soup_dump = [
        (
            'Ноутбук Lenovo IdeaPad 320 15 Intel',
            'Покупателям нравится небольшой вес, мощный процессор',
            'https://avatars.mds.yandex.net/get-mpic/364668/img_id4117518369631908336.jpeg/6hq',
            (
                ('Процессор', 'Core i5 / Core i7'),
                ('Частота процессора', '1600...1800 МГц'),
                ('Объем оперативной памяти', '8...16 ГБ'),
                ('Объем жесткого диска', '256 ГБ'),
                ('Диагональ экрана', '15.6 "'),
            )
        ),
        (
            'Ноутбук Xiaomi Mi Notebook Air 12.5"',
            'Покупателям нравится долгое время работы, небольшой вес',
            'https://avatars.mds.yandex.net/get-mpic/200316/img_id1017256079183483194/6hq',
            (
                ('Процессор', 'Core M3 / Core i3 / Core i5'),
                ('Частота процессора', '900...1200 МГц'),
                ('Объем оперативной памяти', '4...8 ГБ'),
                ('Объем жесткого диска', '128...256 ГБ'),
                ('Диагональ экрана', '12.5 "'),
            )
        ),
    ]

    for product_info in soup_dump:
        obj_product = models.Product.query.filter_by(name=product_info[0]).first()
        if not obj_product:
            obj_product = models.Product(
                name=product_info[0],
                description=product_info[1],
                main_image_path=product_info[2],
            )
        for attribute_info in product_info[3]:
            obj_attribute = models.Attribute.query.filter_by(name=attribute_info[0]).first()
            if not obj_attribute:
                obj_attribute = models.Attribute(
                    name=attribute_info[0],
                )

            p2a = models.ProductAttributes()
            p2a.attribute = obj_attribute
            p2a.product = obj_product
            p2a.value = attribute_info[1]

            db.session.add_all([obj_product, obj_attribute, p2a])

        db.session.commit()

    # a = Association(extra_data="some data")
    # a.child = Child()
    # statement = student_identifier.insert().values(class_id=cl1.id, user_id=sti1.id)
    # db.session.execute(statement)
    # db.session.commit()

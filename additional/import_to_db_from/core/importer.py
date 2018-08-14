import os
import sys

kiosk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if kiosk_path not in sys.path:
    sys.path.append(kiosk_path)

from kiosk.config import db
from kiosk import models


def do_import_products_info_to_database(products_info):
    for product_info in products_info:
        obj_product = models.Product.query.filter_by(
            name=product_info.get('name', 'UNDEF'),
            shop_url=product_info.get('shop_url', 'UNDEF')).first()
        if not obj_product:
            obj_product = models.Product(
                name=product_info.get('name', 'UNDEF'),
                description=product_info.get('description', 'UNDEF'),
                main_image_path=product_info.get('main_image_path', 'UNDEF'),
                shop_url=product_info.get('shop_url', 'UNDEF'),
            )
            db.session.add(obj_product)
            db.session.commit()
        for attribute_info in product_info.get('attrs', []):
            obj_attribute = models.Attribute.query.filter_by(name=attribute_info.get('name', 'UNDEF')).first()
            if not obj_attribute:
                obj_attribute = models.Attribute(
                    name=attribute_info.get('name', 'UNDEF'),
                )
            db.session.add(obj_attribute)
            db.session.commit()

            obj_p2a = models.ProductAttributes.query.filter_by(
                attribute_id=obj_attribute.id,
                product_id=obj_product.id,
            ).first()

            if not obj_p2a:
                obj_p2a = models.ProductAttributes()
                obj_p2a.attribute = obj_attribute
                obj_p2a.product = obj_product
                obj_p2a.value = attribute_info.get('value', 'UNDEF')

                db.session.add(obj_p2a)

        db.session.commit()


if __name__ == '__main__':
    pass

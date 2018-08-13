import os
import sys

kiosk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if kiosk_path not in sys.path:
    sys.path.append(kiosk_path)

from kiosk.config import db


class ProductAttributes(db.Model):
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    attribute_id = db.Column(db.Integer, db.ForeignKey('attribute.id'), primary_key=True)
    value = db.Column(db.String(50))
    product = db.relationship("Product", back_populates="attributes")
    attribute = db.relationship("Attribute", back_populates="products")


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.String(200), nullable=False)
    main_image_path = db.Column(db.String(120), nullable=False)
    attributes = db.relationship("ProductAttributes", back_populates="product")

    def __repr__(self):
        return '<%s %s>' % (self.__class__, self.name)

    def __str__(self):
        return '%s %r' % (self.__class__, self.name)


class Attribute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship("ProductAttributes", back_populates="attribute")

    def __repr__(self):
        return '<%s %s>' % (self.__class__, self.name)

    def __str__(self):
        return '%s %r' % (self.__class__, self.name)


if __name__ == '__main__':
    pass

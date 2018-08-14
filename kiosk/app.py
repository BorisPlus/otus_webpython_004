import os
import sys
from flask import render_template, make_response, redirect, flash, url_for

kiosk_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if kiosk_path not in sys.path:
    sys.path.append(kiosk_path)

from kiosk.config import app, db_path, db
from kiosk.models import Product

if not os.path.exists(db_path):
    db.create_all()


@app.route("/")
@app.route("/products_list")
def products_list():
    return render_template('products_list.html', products=Product.query.all())


@app.route("/product_info/<int:product_id>")
def product_info(product_id):
    product = Product.query.get(product_id)
    if product:
        return render_template('product_info.html', product_id=product_id, product=product)
    else:
        flash('Product with ID %s was not found.' % product_id, 'danger')
        return redirect(url_for('products_list'))


@app.route("/about")
def about():
    return "Kiosk App."


@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = '404 Not found'

    return resp


if __name__ == '__main__':
    app.run()

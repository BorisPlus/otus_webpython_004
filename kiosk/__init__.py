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

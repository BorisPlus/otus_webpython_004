import os
import sys

additional_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if additional_path not in sys.path:
    sys.path.append(additional_path)

from additional.import_to_db_from.core.importer import do_import_products_info_to_database
from additional.import_to_db_from.data.test_data import get_products_info as get_test_products_info
from additional.import_to_db_from.data.mvideo_ru_data import get_products_info as get_mvideo_ru_products_info

if __name__ == '__main__':

    do_import_products_info_to_database(get_test_products_info())

    do_import_products_info_to_database(get_mvideo_ru_products_info())

    for i in range(2, 10):
        url = 'https://www.mvideo.ru/noutbuki-planshety-komputery/noutbuki-118/f/page=%s' % i
        do_import_products_info_to_database(get_mvideo_ru_products_info(url))

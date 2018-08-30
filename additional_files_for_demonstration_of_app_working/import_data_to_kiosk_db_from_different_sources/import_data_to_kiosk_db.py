import os
import sys

additional_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if additional_path not in sys.path:
    sys.path.append(additional_path)

from additional_files_for_demontration_of_app_working.example_import_to_db_from_different_sources.data_importer.importer \
    import do_import_products_info_to_database
from additional_files_for_demontration_of_app_working.example_import_to_db_from_different_sources.data_fetchers.test_data \
    import get_products_info as get_test_products_info
from additional_files_for_demontration_of_app_working.example_import_to_db_from_different_sources.data_fetchers.test_data \
    import get_products_info as get_mvideo_ru_products_info

if __name__ == '__main__':

    # Offline import prepared test data
    do_import_products_info_to_database(get_test_products_info())

    # Online import data to KIOSK from Mvideo site
    do_import_products_info_to_database(get_mvideo_ru_products_info())

    for i in range(2, 10):
        url = 'https://www.mvideo.ru/noutbuki-planshety-komputery/noutbuki-118/f/page=%s' % i
        do_import_products_info_to_database(get_mvideo_ru_products_info(url))

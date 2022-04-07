import json
from selenium.webdriver.common.by import By
from downloads_settings import driver_call
from update_monitor import last_update_info

TICKERS_JSON_PATH = '/home/nick/ANAL_ISIS/anal_isis/download_manager/download_files/tickers_folder/tickers.json'
def download_new_tikers_json():
    '''
    1. don't show display page downlaod
    2. .'sleep' convert into "display when ot can be possible
    '''
    tickers_url = 'https://www.sec.gov/files/company_tickers.json'

    try:
        driver = driver_call()
        driver.get(tickers_url)
        page_1 = driver.find_element(By.TAG_NAME, "body")
        tikers_dict = json.loads(page_1.text)
        driver.quit()
        return tikers_dict
    except:
        pass
    finally:
        print('DONE')

def write_tikers_doc(tickers_dict):
    with open(TICKERS_JSON_PATH, 'w') as outfile:
        json.dump(tickers_dict, outfile)
        return 'done'
# print(display_file_update_status(TICKERS_JSON_PATH))

tickers_dict = download_new_tikers_json()




write_tikers_doc(tickers_dict)
print(last_update_info(TICKERS_JSON_PATH))
# strftime('%Y-%m-%d'))
# def main():
#     today
#
#     if today > check_date():
#         download_new_tikers_json()
#     with open (tickers_json_path) as file:
#         return file.read()



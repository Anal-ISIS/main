import os
import datetime

download_folder_path = '/home/nick/ANAL_ISIS/anal_isis/download_manager/download_files/tickers_folder'


def display_all_download_status(folder_path):
    see_files = os.listdir(folder_path)
    files_update_status = {}
    for file in see_files:
        day_last_change_stamp = os.path.getmtime(folder_path + '/' + file)
        day_last_change_date = datetime.datetime.fromtimestamp(day_last_change_stamp).strftime('%Y-%m-%d %H:%M:')
        files_update_status.update({file: day_last_change_date})
    return files_update_status


def last_update_info(file_path):
    day_last_change_stamp = os.path.getmtime(file_path)
    day_last_change_date = datetime.datetime.fromtimestamp(day_last_change_stamp)
    file_name = file_path.split('/')[-1]

    day = day_last_change_date.strftime('%Y-%m-%d')
    detail = day_last_change_date.strftime('%Y-%m-%d %H:%M:')
    return {file_name:day}
# {file_name:{'day':day,'detail':detail}}

# print(display_all_download_status(download_folder_path))

# class FILE:
#     def __init__(self, file_path):
#         self.file_name = file_path.split('/')[-1]
#         self.file_path = file_path
#
#         self.last_update = last_update_info()
#         self.last_update_day = self.last_update.strftime('%Y-%m-%d %H:%M:')
#         # self.last_update_detail =
#
#     def last_update_info(self):
#         file_path = self.file_path
#         day_last_change_stamp = os.path.getmtime(file_path)
#         day_last_change_date = datetime.datetime.fromtimestamp(day_last_change_stamp)
#         return (day_last_change_date)


# ({self.file_name:
# noth = FILE(download_folder_path)

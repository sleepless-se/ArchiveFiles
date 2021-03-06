import os
import datetime
import shutil
import logging
import datetime

# settings
DAYS = 7
HOME_PATH = os.environ['HOME']
DESKTOP_PATH = os.path.join(HOME_PATH, "Desktop")
DOWNLOADS_PATH = os.path.join(HOME_PATH, "Downloads")
ARCHIVE_FOLDER_NAME = "Archive"
REMOVE_LIST = ['']

# #logging
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FOLDER_PATH = os.path.join(ROOT_DIR, "log")
LOG_FILE_PATH = os.path.join(LOG_FOLDER_PATH, "info.log")
logging.basicConfig(filename=LOG_FILE_PATH, level=logging.INFO)



def move_to(current_path, oldFolder, days=7):
    logging.debug(current_path)
    dir = os.listdir(current_path)
    today = datetime.date.today().strftime("%Y-%m-%d")
    archive_folder = os.path.join(current_path, oldFolder)
    if not os.path.exists(archive_folder):os.mkdir(archive_folder)
    archive_folder = os.path.join(archive_folder,today)
    if not os.path.exists(archive_folder): os.mkdir(archive_folder)
    dead_line = datetime.date.today() - datetime.timedelta(days=days)
    logging.debug(dead_line)

    for file_name in dir:
        logging.info("file_name:{}".format(file_name))
        target = os.path.join(current_path, file_name)
        logging.debug(target)

        if target in REMOVE_LIST:
            logging.debug('remove list name')
            continue

        if os.path.exists(target):
            dt = datetime.datetime.fromtimestamp(os.stat(target).st_mtime)
        key = dt.strftime('%Y/%m/%d  %H:%M:%S')
        logging.debug(str(key) + " - " + str(dt))


        if (dt.date() < dead_line):
            try:
                shutil.move(target, archive_folder)
            except Exception as e:
                logging.warning(e)
                shutil.rmtree(archive_folder)
                shutil.move(target, archive_folder)
            logging.info("moved")
        else:
            logging.info("keep")

    logging.warning("Can't open " + file_name)

    logging.debug("- - -")

if __name__ == '__main__':
    move_to(DOWNLOADS_PATH, ARCHIVE_FOLDER_NAME, DAYS)
    move_to(DESKTOP_PATH, ARCHIVE_FOLDER_NAME, DAYS)

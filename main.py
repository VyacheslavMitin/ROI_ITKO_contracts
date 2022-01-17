# Модуль считывания договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time
import configparser
from datetime import datetime

# Константы
cfg = configparser.ConfigParser()
cfg.read('config.ini')
TIMES = int(cfg.get('SETTS', 'strings'))
SLEEP_TABS = float(cfg.get('SETTS', 'pause'))
FILE_NAME = cfg.get('SETTS', 'name_file')
FILE_NAME_XLSX = f"{FILE_NAME[:-4]}_{datetime.now().strftime('%d.%m.%Y_%H-%M')}.xlsx"


# Функции
def eng_layout():
    pg.hotkey('ctrl', '8')
    time.sleep(0.5)


def rus_layout():
    pg.hotkey('ctrl', '9')
    time.sleep(0.5)


def generating_file():
    with open(FILE_NAME, 'w') as file_dummy:
        file_dummy.write('N,Контрагент,Банк-партнер,Название договора,Начало периода,Конец периода' + '\n')

    time.sleep(2)
    pg.press('up', presses=1500)
    pg.press('left', presses=20)

    for item in range(TIMES):
        if item != 0:
            pg.press('down', presses=1)

        time.sleep(0.2)

        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(str(item + 1))
            file_reports.write(",")

        time.sleep(0.2)

        pg.press('tab', presses=5)

        pg.hotkey("ctrl", "c")
        name_contragent = pyperclip.paste()
        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(name_contragent)
            file_reports.write(",")

        pg.keyDown('shift')
        pg.press('tab', presses=3)
        pg.keyUp('shift')
        time.sleep(SLEEP_TABS)

        pg.hotkey("ctrl", "c")
        bank_partner = pyperclip.paste()
        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(bank_partner)
            file_reports.write(",")

        pg.keyDown('shift')
        pg.press('tab', presses=1)
        pg.keyUp('shift')
        time.sleep(SLEEP_TABS)

        pg.hotkey("ctrl", "c")
        name_contract = pyperclip.paste()
        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(name_contract)
            file_reports.write(",")

        pg.press('tab', presses=5)
        time.sleep(SLEEP_TABS)

        pg.hotkey("ctrl", "c")
        date_contract_start = pyperclip.paste()
        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(date_contract_start)
            file_reports.write(",")

        pg.press('tab')
        time.sleep(SLEEP_TABS)

        pg.hotkey("ctrl", "c")
        date_contract_finish = pyperclip.paste()
        with open(FILE_NAME, 'a') as file_reports:
            file_reports.write(date_contract_finish)
            file_reports.write('\n')
        time.sleep(SLEEP_TABS)

        pg.press('left', presses=20)


def converting_file():
    from xlsxwriter.workbook import Workbook
    import csv

    workbook = Workbook(FILE_NAME_XLSX)
    worksheet = workbook.add_worksheet(FILE_NAME_XLSX[:-5])
    with open(FILE_NAME, 'rt') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader):
            for c, col in enumerate(row):
                worksheet.write(r, c, col)
    workbook.close()


def deleting_file_csv():
    import os
    time.sleep(1)
    os.remove(FILE_NAME)
    time.sleep(1)


def opening_xlsx():
    import os
    os.system(FILE_NAME_XLSX)


if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    rus_layout()
    generating_file()
    converting_file()
    # deleting_file_csv()
    opening_xlsx()
    # pg.alert('Сделано')

#  Модуль считывания договоров с ИТКО

import pyautogui as pg
import pyperclip
import time
import configparser


# Константы
cfg = configparser.ConfigParser()
cfg.read('config.ini')
TIMES = int(cfg.get('SETTS', 'strings'))
SLEEP_TABS = float(cfg.get('SETTS', 'pause'))
FILE_NAME = cfg.get('SETTS', 'name_file')


# Функции
def eng_layout():
    pg.hotkey('ctrl', '8')
    time.sleep(0.5)


def rus_layout():
    pg.hotkey('ctrl', '9')
    time.sleep(0.5)


def main():
    with open(FILE_NAME, 'w') as file_dummy:
        file_dummy.write('Контрагент,Банк-партнер,Название договора,Начало периода,Конец периода' + '\n\n')

    time.sleep(2)
    pg.press('up', presses=400)
    pg.press('left', presses=20)

    for item in range(TIMES):
        if item != 0:
            pg.press('down', presses=1)

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


if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    rus_layout()
    main()
    pg.alert('Сделано')

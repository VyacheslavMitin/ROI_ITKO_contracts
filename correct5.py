# Модуль коррекции договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time


# Константы
TIMES = 1000
TUPLE_OLD_BANKS = ()  # ('venec',)
TUPLE_CURRENT_BANKS = ('vbrr', 'gpb', 'rinkas',)


# Функции
def eng_layout():
    pg.hotkey('ctrl', '8')
    time.sleep(0.5)


def rus_layout():
    pg.hotkey('ctrl', '9')
    time.sleep(0.5)


def change_layout():
    pg.keyDown('alt')
    pg.press('shift')
    pg.keyUp('alt')


def correcting_contracts():
    time.sleep(0.5)
    pg.press('up', presses=1500)
    pg.press('left', presses=20)
    time.sleep(0.5)
    pg.press('right', presses=7)
    change_layout()
    time.sleep(0.1)

    for item in range(TIMES):
        pg.hotkey('ctrl', 'c')
        date_finish = pyperclip.paste()
        # try:
        #     _, _, date_year = date_finish.split('.')
        # except ValueError:
        #     pg.click(2140, 230)
        #     pg.hotkey('ctrl', 'c')
        #     date_finish = pyperclip.paste()
        _, _, date_year = date_finish.split('.')

        print(date_finish)

        if date_year in ('21', '22',):
            pg.press('left', presses=5)
            pg.hotkey('ctrl', 'c')
            bank = pyperclip.paste()
            print(bank)
            if bank in TUPLE_OLD_BANKS:
                pg.press('right', presses=5)
                time.sleep(0.5)
                pg.hotkey('ctrl', 'c')
                time.sleep(0.5)
                pg.press('enter')  # вход в договор
                time.sleep(1)
                pg.click(650, 400)  # клик на поле с датой конца периода
                pg.press('backspace', presses=10)
                time.sleep(0.2)
                change_layout()
                pg.write('30.09.20')
                time.sleep(0.5)
                pg.click(70, 725)  # клик на кнопке сохранить
                time.sleep(1)
                pg.press('space')
                time.sleep(2)
                pg.press('space')
                time.sleep(2)
                # pg.click(2140, 230)  # клик на столбце и первой строке в окон. периоде в журнале
                # time.sleep(0.5)
                pg.press('esc', presses=3)
                time.sleep(0.5)
                # pg.press('right', presses=5)
                pg.press('down', presses=item)
                time.sleep(0.5)
            elif bank in TUPLE_CURRENT_BANKS:
                pg.press('right', presses=5)
                time.sleep(0.5)
                pg.hotkey('ctrl', 'c')
                time.sleep(0.5)
                pg.press('enter')  # вход в договор
                time.sleep(1)
                pg.click(650, 400)  # клик на поле с датой конца периода
                pg.press('backspace', presses=10)
                time.sleep(0.2)
                change_layout()
                pg.write('30.06.25')
                time.sleep(0.5)
                pg.click(70, 725)  # клик на кнопке сохранить
                time.sleep(1)
                pg.press('space')
                time.sleep(2)
                pg.press('space')
                time.sleep(2)
                # pg.click(2140, 230)  # клик на столбце и первой строке в окон. периоде в журнале
                # time.sleep(0.5)
                pg.press('esc', presses=3)
                time.sleep(0.5)
                # pg.press('right', presses=5)
                pg.press('down', presses=item)
                time.sleep(0.5)
            else:
                pg.press('right', presses=5)
                pg.press('down')
        elif date_finish in TUPLE_OLD_BANKS or date_finish in TUPLE_CURRENT_BANKS:
            pg.press('right', presses=5)
            pg.hotkey('ctrl', 'c')
            date_finish = pyperclip.paste()
        else:
            pg.press('down')


if __name__ == '__main__':
    start_time = time.time()
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    # rus_layout()
    correcting_contracts()
    print("--- %s seconds ---" % (time.time() - start_time))
    pg.alert('Сделано')

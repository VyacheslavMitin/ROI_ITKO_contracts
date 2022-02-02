# Модуль коррекции договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time

from dates import TUPLE_DATES, DATE

# Константы
TIMES = 5000


# Функции
def eng_layout():
    pg.hotkey('ctrl', '8')
    time.sleep(0.5)


def rus_layout():
    pg.hotkey('ctrl', '9')
    time.sleep(0.5)


def correcting_contracts():
    time.sleep(1)
    pg.press('up', presses=1500)
    pg.press('left', presses=20)
    time.sleep(0.5)
    pg.press('right', presses=2)

    time.sleep(0.1)
    for item in range(TIMES):
        pg.hotkey('ctrl', 'c')
        bank = pyperclip.paste()
        print(bank)
        if bank == 'venec':
            time.sleep(0.5)
            pg.press('right', presses=5)
            pg.hotkey('ctrl', 'c')
            date_finish = pyperclip.paste()
            _, _, date_year = date_finish.split('.')
            tuple_ = ('21', '22', '23', '24', '25', '26')
            if date_year in tuple_:
                pg.press('enter')  # вход в договор
                time.sleep(1)
                pg.click(650, 400)  # клик на поле с датой конца периода
                pg.press('backspace', presses=10)
                time.sleep(0.2)
                pg.write('30.09.20')
                time.sleep(0.5)
                pg.click(70, 725)  # клик на кнопке сохранить
                time.sleep(1)
                pg.press('space')
                time.sleep(1)
                pg.press('space')
                time.sleep(2)
                pg.press('esc')
                pg.press('left', presses=5)
                pg.press('down')
            else:
                pg.press('left', presses=5)
                pg.press('down')

        else:
            pg.press('down')




if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    eng_layout()
    correcting_contracts()

    pg.alert('Сделано')

# Модуль коррекции договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time

from dates import TUPLE_DATES, DATE

# Константы
TIMES = 181


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
    pg.hotkey('ctrl', 'f3')
    time.sleep(0.1)
    pg.press('delete', presses=15)
    time.sleep(0.1)
    pg.write('venec')
    time.sleep(1)
    pg.press('enter')
    for i in range(TIMES):
        # press = i
        time.sleep(0.5)
        pg.click(470, 66, clicks=i, interval=0.5)
        # pg.keyDown('shift')
        # time.sleep(1)
        # pg.hotkey('f3', interval=0.5, presses=press)
        # print(press)
        # pg.keyUp('shift')
        time.sleep(1)
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
        # pg.click(1220, 760)  # клик на кнопке пересчета даты
        time.sleep(1)
        pg.press('space')
        time.sleep(2)
        pg.press('esc')
        # pg.click(1220, 760)  # клик на всякий случай если договор дубль есть
        # time.sleep(1)
        # pg.click(2140, 230)  # клик на столбце и первой строке в окон. периоде в журнале
        # time.sleep(0.5)
        # i += 1



if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    eng_layout()
    correcting_contracts()

    pg.alert('Сделано')

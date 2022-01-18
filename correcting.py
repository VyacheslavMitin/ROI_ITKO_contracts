# Модуль коррекции договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time


# Константы
TIMES = 50


LIST_ = [
'01.04.22','30.06.22','01.03.22','01.04.22','01.02.22','01.04.22','01.03.22','01.04.22','05.03.22','01.01.23','31.10.22','01.06.22','01.01.22','04.04.22','01.09.22','05.03.22','01.06.22','05.03.22','30.11.22','31.07.22','01.11.22','01.01.23','01.02.22','01.04.22','01.04.22','01.08.22','01.01.23','30.09.22','01.12.22','01.02.22','01.11.22','15.03.22','21.07.22','01.05.22','01.06.22','01.05.22']


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
    pg.press('right', presses=7)

    for i in range(TIMES):
        pg.press('down')
        time.sleep(0.1)
        pg.hotkey("ctrl", "c")
        if pyperclip.paste() in LIST_:
            pg.press('enter')
            time.sleep(1)
            pg.click(650, 400)
            pg.press('backspace', presses=10)
            pg.write('30.06.25')
            time.sleep(1)
            pg.click(70, 725)
            time.sleep(1)
            pg.press('space')
            time.sleep(3)
            # pg.press('tab', presses=2, interval=0.5)
            # pg.hotkey("ctrl", "c")
            # if pyperclip.paste() == 'Нет' or 'Да':
            #     pass
            # else:
            #     pg.press('esc')
            # pg.press('tab', presses=9, interval=0.5)
            # pg.write('30.06.25')
            # pg.press('tab', presses=1, interval=0.5)
            # pg.press('space')
            # time.sleep(1)
            # pg.press('space')
            # pg.press('tab', presses=1, interval=0.5)
            # time.sleep(2)
            # pg.keyDown('shift')
            # pg.press('tab', presses=10, interval=0.5)
            # pg.keyUp('shift')
            # if pyperclip.paste() == 'Нет' or 'Да':
            #     pass
            # else:
            #     pg.press('esc')
            # pg.press('tab', presses=5, interval=0.5)
            # input()


if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    rus_layout()
    correcting_contracts()

    pg.alert('Сделано')

# Модуль коррекции договоров с ИТКО
# Предварительно должна быть запущена ИТКО и открыт справочник договоров

import pyautogui as pg
import pyperclip
import time

from dates import TUPLE_DATES, DATE

# Константы
TIMES = 10000


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

    for item in TUPLE_DATES:
        time.sleep(0.1)
        pg.hotkey('ctrl', 'f3')
        time.sleep(0.1)
        pg.press('delete', presses=15)
        time.sleep(0.1)
        pg.write(item)
        time.sleep(1)
        pg.press('enter')
        time.sleep(1)
        # input()
        # if pyperclip.paste() in TUPLE_DATES:
        pg.press('enter')  # вход в договор
        time.sleep(1)
        # input()
        pg.click(650, 400)  # клик на поле с датой конца периода
        pg.press('backspace', presses=10)
        time.sleep(0.2)
        pg.write(DATE)
        time.sleep(0.5)
        pg.click(70, 725)  # клик на кнопке сохранить
        time.sleep(1)
        pg.click(1220, 760)  # клик на кнопке пересчета даты
        time.sleep(1)
        pg.click(1220, 760)  # клик на всякий случай если договор дубль есть
        time.sleep(1)
        pg.click(2140, 230)  # клик на столбце и первой строке в окон. периоде в журнале
        time.sleep(0.5)
            # break
            # time.sleep(1)
            # pg.press('space')
            # time.sleep(3)
            # pg.press('down', presses=i+1)
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
        # else:
        #     pg.press('down')


if __name__ == '__main__':
    pg.keyDown('alt')
    pg.press('tab')
    pg.keyUp('alt')
    eng_layout()
    correcting_contracts()

    pg.alert('Сделано')

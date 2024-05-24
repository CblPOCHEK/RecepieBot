from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def get_keyboard_1():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = KeyboardButton('Рецепт пиццы')
    button_2 = KeyboardButton('Перейти к другому рецепту')
    keyboard.add(button_1, button_2)
    return keyboard
def get_keyboard_2():
    keyboard_2 = ReplyKeyboardMarkup(resize_keyboard=True)
    button_3 = KeyboardButton('Рецепт лазаньи')
    button_4 = KeyboardButton('Вернуться к рецепту лазаньи')
    keyboard_2.add(button_3, button_4)
    return keyboard_2
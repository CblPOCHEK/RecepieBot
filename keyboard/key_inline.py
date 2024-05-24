from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton(text='Посмотреть', url='https://1000.menu/cooking/6190-pitstsa-pepperoni-')
    keyboard_inline.add(but_inline)
    return keyboard_inline

def get_keyboard_inline_2():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline2 = InlineKeyboardButton(text='Посмотреть', url='https://1000.menu/cooking/30072-lazanya-boloneze')
    keyboard_inline.add(but_inline2)
    return keyboard_inline
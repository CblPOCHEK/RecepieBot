from aiogram import Bot, Dispatcher, types, executor
from keyboard.keyboard import get_keyboard_1, get_keyboard_2
from keyboard.key_inline import get_keyboard_inline

bot = Bot (token = '6764754713:AAH4ZZeZkJUytUAszB1ATts9wu79VB7250M')
dp = Dispatcher (bot)

@dp.message_handler (commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я бот с рецептами!',reply_markup=get_keyboard_1())


@dp.message_handler (lambda message: message.text == 'Рецепт пиццы')
async def button_1_click(message: types.Message) :
    await bot.send_photo(message.chat.id, photo= 'https://www.tokyo-city.ru/images/interesno/Pitctca_-_natcionalnoe_italyanskoe_blyudo.jpg',caption='Вот рецепт пиццы', reply_markup=get_keyboard_inline())

@dp.message_handler (lambda message: message.text == 'Перейти к другому рецепту')
async def button_2_click(message: types.Message) :
    await message.answer(text = 'Тут вы можете посмотреть рецепт лазаньи', reply_markup= get_keyboard_2())

@dp.message_handler (lambda message: message.text == 'Рецепт лазаньи')
async def button_3_click(message: types.Message) :
    await bot.send_photo(message.chat.id, photo= 'https://www.patee.ru/r/x6/15/62/40/640m.jpg',caption='Вот рецепт лазаньи', reply_markup=get_keyboard_inline())

@dp.message_handler (lambda message: message.text == 'Вернуться к рецепту лазаньи')
async def button_4_click(message: types.Message) :
    await message.answer(text = 'Тут вы можете посмотреть рецепт пиццы', reply_markup= get_keyboard_1())

if __name__ == '__main__':
    executor. start_polling(dp, skip_updates= True)
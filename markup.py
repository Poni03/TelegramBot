from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup


#MAin menu
btDMD = KeyboardButton('Новая тема')
btProfile = KeyboardButton('👤 Профиль')
btBuy = KeyboardButton('💎Оформить подписку')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btProfile, btBuy)
mainDMD = ReplyKeyboardMarkup(resize_keyboard = True)
mainDMD.add(btDMD, btProfile, btBuy)

#InlineMenu
InlineMenu = InlineKeyboardMarkup(row_width = 2)
InlineFinish = InlineKeyboardButton(text="Завершить диалог", callback_data="InlineFinish")

InlineMenu.insert(InlineFinish)

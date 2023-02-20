from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from aiogram.utils.callback_data import CallbackData
from configurebot import cfg
from aiogram import types
from bot import dp, bot


errormessage = cfg['error_message']
devid = cfg['dev_id']


async def send_Podrob(callback: types.CallbackQuery):
        try:
                
                await callback.answer()
        except Exception as e:
                await callback.message.answer(f"{errormessage}",
                             parse_mode='Markdown')
                await bot.send_message(devid, f"Случилась *ошибка* в чате **\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')

async def send_recenz(callback: types.CallbackQuery):
        try:
                
                await callback.answer()
        except Exception as e:
                await callback.message.answer(f"{errormessage}",
                             parse_mode='Markdown')
                await bot.send_message(devid, f"Случилась *ошибка* в чате **\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')

async def send_statis(callback: types.CallbackQuery):
        try:
                
                await callback.answer()
        except Exception as e:
                await callback.message.answer(f"{errormessage}",
                             parse_mode='Markdown')
                await bot.send_message(devid, f"Случилась *ошибка* в чате **\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')

async def send_previous(callback: types.CallbackQuery):
        try:
                
                await callback.answer()
        except Exception as e:
                await callback.message.answer(f"{errormessage}",
                             parse_mode='Markdown')
                await bot.send_message(devid, f"Случилась *ошибка* в чате **\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')






Menu = InlineKeyboardMarkup(row_width=2, resize_keyboard=True,
        inline_keyboard=[
                [
                InlineKeyboardButton(   
                        text=('Подробнее'),
                        callback_data='Podrob'
                        ),
                
                InlineKeyboardButton(
                        text="Купить",
                        url = "https://igraslov.store/product/gegel-g-v-f-nauka-logiki-ast-populyarnaya-filosofiya-s-illyustracziyami-tverd/"
                        ),
                ],
                [
                InlineKeyboardButton(
                        text="Отзыв",
                        callback_data='recenz'
                        ),
                
                
                InlineKeyboardButton(
                        text="Статистика",
                        callback_data='statis'
                        )
                ],
                [                
                InlineKeyboardButton(
                        text="Предыдущая",
                        callback_data='previous'
                        ),
                
                InlineKeyboardButton(
                        text="Следующая",
                        callback_data='next'
                        )
                ],

        ]
)

startbut = InlineKeyboardButton(
        text=('Статистика'),
        callback_data='statistic',
        )

statistic = InlineKeyboardMarkup()
statistic.add(startbut)

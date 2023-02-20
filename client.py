from aiogram import types
import kb
from bot import dp, bot
from handlers.fsm import *
from handlers.db import *
from configurebot import cfg
from aiogram.types import callback_query
from aiogram.utils.callback_data import CallbackData


welcomemessage = cfg['welcome_message']
errormessage = cfg['error_message']
devid = cfg['dev_id']


async def client_start(message: types.Message):
    try:
        if(message.chat.type != 'private'):
            await message.answer('Данную команду можно использовать только в личных сообщениях с ботом.')
            return
        elif db_profile_exist(message.from_user.id):
            await message.answer(f'{welcomemessage}',parse_mode='Markdown', reply_markup=kb.Menu)
            
        else:
            db_profile_insertone({'_id': message.from_user.id})
            print('Новый пользователь!')
            await message.answer(f'{welcomemessage}',parse_mode='Markdown', reply_markup=kb.Menu)

    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')

async def push_next(message: types.Message):
    try:
        if db_profile_info(message.from_user.id) == db_book_pages():
            await message.answer(f"Все книги на данный момент просмотрены, рекомендуем посмотреть статистику:", reply_markup = kb.statistic)
        else:
            db_page_next(db_profile_info(message.from_user.id), message.from_user.id)

    except Exception as e:
        cid = message.chat.id
        await message.answer(f"{errormessage}",
                             parse_mode='Markdown')
        await bot.send_message(devid, f"Случилась *ошибка* в чате *{cid}*\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')


async def send_next(callback: types.CallbackQuery):
        try:
                await push_next()
                await callback.answer()
        except Exception as e:
                await callback.message.answer(f"{errormessage}",
                             parse_mode='Markdown')
                await bot.send_message(devid, f"Случилась *ошибка* в чате **\nСтатус ошибки: `{e}`",
                               parse_mode='Markdown')


def register_handler_client():
    dp.register_message_handler(client_start, commands='start')
    dp.register_callback_query_handler(kb.send_Podrob, text="Podrob")
    dp.register_callback_query_handler(kb.send_recenz, text="recenz")
    dp.register_callback_query_handler(kb.send_statis, text='statis')
    dp.register_callback_query_handler(kb.send_previous, text="previous" )
    dp.register_callback_query_handler(send_next, text="next")
#    dp.register_callback_query_handler(push_next, text='next')
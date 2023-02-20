from bot import dp, bot
from aiogram.utils import executor
from handlers import client, admin, fsm
import logging
from aiogram import Bot, Dispatcher, executor, types

#admin.register_handler_admin()
#fsm.register_handler_FSM()
client.register_handler_client()

executor.start_polling(dp, skip_updates=True)
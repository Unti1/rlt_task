# Telegram bot modules

from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.exceptions import TelegramBadRequest
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command
from aiogram import Bot, Dispatcher
from aiogram.fsm.state import  State, StatesGroup
from aiogram.fsm.context import  FSMContext
from aiogram import Router, F
from aiogram import types

# Some asyn modules

import asyncio

# Settings 'n logging modules
import configparser
import traceback
import logging

# MongoDB modules(async)
from motor.motor_asyncio import AsyncIOMotorClient

# Time modules
from datetime import datetime,timezone,timedelta

# Others modules 
import json


config = configparser.ConfigParser()
config.read('settings/settings.ini')

def update_config():
    with open('settings/settings.ini') as fl:
        config.write(fl)
    config.read('settings/settings.ini')


TIMEZONE = timezone(timedelta(hours=3),'Europe/Moscow')

logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    format="%(asctime)s - %(module)s\n[%(levelname)s] %(funcName)s:\n %(lineno)d - %(message)s",
    datefmt='%H:%M:%S',
    encoding="utf-8"
)


    
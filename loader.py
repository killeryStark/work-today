from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data import config
from utils.db_api.mongo import Database
# from utils.expenses.expenses import CreateExpenses
from utils.task import Tasks

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
db = Database()
tasks = Tasks()
# expenses = CreateExpenses()

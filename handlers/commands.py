from settings import *

router = Router()

@router.message(Command('start'))
async def send_welcome(message: types.Message):
    # Starting message
    await message.reply("Привет! Я бот для агрегации статистических данных. Отправьте мне данные в формате JSON.")


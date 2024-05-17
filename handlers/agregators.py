from settings import *

router = Router()

@router.message(F.text)
async def process_json(message: types.Message):
    from tools.db_agregator import aggregate_salaries
    try:
        # JSON parse
        data = json.loads(message.text)
        # agregating
        result = await aggregate_salaries(**data)
        # send result
        await message.answer(json.dumps(result, ensure_ascii=False))
    
    except json.JSONDecodeError:
        await message.reply("Пожалуйста, отправьте данные в правильном формате JSON.")
    
    except KeyError as e:
        await message.reply(f"Отсутствует необходимый ключ в данных: {e}")
    
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
        logging.error(traceback.format_exc())
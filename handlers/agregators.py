from settings import *

router = Router()

@router.message(F.text)
async def process_json(message: types.Message):
    pass
    
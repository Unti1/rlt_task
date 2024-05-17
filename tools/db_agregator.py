from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

async def aggregate_salaries(dt_from, dt_upto, group_type):
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    db = client.MyDB
    collection = db.sample_collection

    group_format = {
        'hour': '%Y-%m-%dT%H:00:00',
        'day': '%Y-%m-%dT00:00:00',
        'month': '%Y-%m-01T00:00:00'
    }[group_type]

    return {'dataset': filled_dataset, 'labels': filled_labels}


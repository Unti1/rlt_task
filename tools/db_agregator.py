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

    pipeline = [
        {"$match": {"dt": {"$gte": datetime.fromisoformat(dt_from), "$lte": datetime.fromisoformat(dt_upto)}}},
        {"$group": {"_id": {"$dateToString": {"format": group_format, "date": "$dt"}}, "totalAmount": {"$sum": "$value"}}},
        {"$sort": {"_id": 1}},
        {"$project": {"_id": 0, "label": "$_id", "totalAmount": 1}}
    ]

    cursor = collection.aggregate(pipeline)
    dataset, labels = [], []
    async for doc in cursor:
        labels.append(doc['label'])
        dataset.append(doc['totalAmount'])

    # Дополнение недостающих дат с нулевыми значениями
    current_date = datetime.fromisoformat(dt_from)
    end_date = datetime.fromisoformat(dt_upto)
    filled_dataset, filled_labels = [], []
    
    while current_date <= end_date:
        str_date = current_date.strftime(group_format)
        if str_date in labels:
            index = labels.index(str_date)
            filled_dataset.append(dataset[index])
        else:
            filled_dataset.append(0)
        filled_labels.append(str_date)
        
        if group_type == 'hour':
            current_date += timedelta(hours=1)
        elif group_type == 'day':
            current_date += timedelta(days=1)
        elif group_type == 'month':
            current_date += relativedelta(months=+1)
    
    return {'dataset': filled_dataset, 'labels': filled_labels}


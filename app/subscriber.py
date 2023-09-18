import base64
import json

from fastapi import APIRouter, Request
from google.cloud.pubsub_v1.subscriber.message import Message

router = APIRouter()


@router.post("/subscribe")
async def subscriber(request: Request):
    data = await request.body()
    envelope: Message = json.loads(data)
    message = envelope["message"]["data"]
    payload = base64.b64decode(message).decode()
    print(f'Received event: {payload}')
    # logging.info(f'Received message: {message}')

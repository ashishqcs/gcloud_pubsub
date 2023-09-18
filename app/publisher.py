from fastapi import APIRouter
from google.cloud import pubsub_v1
from pydantic import BaseModel

router = APIRouter()
publisher = pubsub_v1.PublisherClient()
topic_name = 'projects/{project_id}/topics/{topic}'.format(
    project_id='GCP-learning',
    topic='test-topic',  # Set this to something appropriate.
)


class Message(BaseModel):
    title: str


@router.post("/publish")
async def publish_to_pubsub(message: Message):
    publish(message.title)
    return "published"


def publish(title: str):
    byte_message = title.encode()
    future = publisher.publish(topic_name, byte_message)
    future.result()

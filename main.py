import logging

import uvicorn
from fastapi import FastAPI
from app.publisher import router
from app.subscriber import router as sub_router

logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(router)
app.include_router(sub_router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080, access_log=True, log_config='log_conf.yml')


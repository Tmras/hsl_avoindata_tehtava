import os
import signal

import uvicorn
from fastapi import FastAPI

import real_time_data
import saved_data

app = FastAPI()


@app.get("/realtime/{f_id}")
async def get_realtime(f_id):
    return real_time_data.get_data(f_id)


@app.get("/saved/{f_id}")
async def get_realtime(f_id):
    return saved_data.get_data(f_id)


def start_api():
    uvicorn.run(app, host="127.0.0.1", port=8000)


def shutdown_api():
    os.kill(os.getpid(), signal.SIGTERM)

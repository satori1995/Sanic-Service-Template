"""
创建 Sanic APP
"""
from sanic import Sanic
from lib.app_core.global_context import global_context
from lib.settings import SERVICE_NAME

app = Sanic(SERVICE_NAME)


# 心跳检测，用于验证服务是否正常
@app.get("/state/healthcheck")
async def healthcheck(_):
    global_context.response_data.set(
        code=200,
        data={},
        error_message="",
        traceback=""
    )
    return global_context.response_data.response

from fastapi import FastAPI
import time


class TimingMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        start_time = time.time()
        await self.app(scope, receive, send)
        duration = time.time() - start_time
        print(f"Request duration: {duration:.10f} seconds")


app = FastAPI()
app.add_middleware(TimingMiddleware)


@app.get("/hello")
async def greeter():
    return {"Hello": "World"}


@app.get("/goodbye")
async def farewell():
    return {"Goodbye": "World"}
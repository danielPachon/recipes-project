from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from starlette.responses import RedirectResponse
from helpers.api_key_auth import get_api_key
from routes.user_route import user_router
from config.database import database as connection


@asynccontextmanager
async def manage_lifespan(_app: FastAPI):
    if connection.is_closed():
        connection.connect()
    try:
        yield
    finally:
        await connection.is_closed()
        connection.close()


app = FastAPI(
    title="recipes-project",
    version="1.0",
    contact={
        "url": "https://github.com/danielPachon/recipes-project.git",
    },
    lifespan=manage_lifespan,
)


@app.get("/", include_in_schema=False)
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(
    user_router,
    prefix="/users",
    tags=["users"],
    dependencies=[Depends(get_api_key)],
)

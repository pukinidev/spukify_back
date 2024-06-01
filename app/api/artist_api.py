from fastapi import FastAPI
from routers import artist_router

artistsapi = FastAPI()

artistsapi.include_router(artist_router.router)
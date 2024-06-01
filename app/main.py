# Server 
import uvicorn

# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routers import users_router, tracks_router, albums_router, artists_router
from config.database import engine
from models import track_model, user_model, album_model, artist_model

app = FastAPI(
    title="Spukify Backend",
    description="This is the backend for the Spukify project",
)

track_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
album_model.Base.metadata.create_all(bind=engine)
artist_model.Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.include_router(users_router.users_router)
app.include_router(artists_router.artists_router)


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
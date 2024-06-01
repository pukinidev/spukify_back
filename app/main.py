# Server 
import uvicorn

# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from apis import user_api, artist_api, album_api, track_api
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

# Define the API routes
app.mount("/users", user_api.usersapi)
app.mount("/artists", artist_api.artistsapi)
app.mount("/albums", album_api.albumsapi)
app.mount("/tracks", track_api.tracksapi)

# Redirect to /docs
@app.get("/users", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="users/docs")

@app.get("/artists", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="artists/docs")

@app.get("/albums", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="albums/docs")

@app.get("/tracks", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="tracks/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
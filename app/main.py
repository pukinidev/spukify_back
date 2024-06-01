# Server 
import uvicorn

# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routers import user_router, track_router, playlist_router, album_router, artist_router, category_router

app = FastAPI(
    title="Spukify Backend",
    description="This is the backend for the Spukify project",
)

app.include_router(user_router.router)
app.include_router(track_router.router)
app.include_router(playlist_router.router)
app.include_router(album_router.router)
app.include_router(artist_router.router)
app.include_router(category_router.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

@app.get("/")
def main_function():
    return RedirectResponse(url="/docs/")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
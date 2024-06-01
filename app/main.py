# Server 
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from routers import users_router, artists_router
from config.database import engine
from models import track_model, user_model, album_model, artist_model

app = FastAPI(
    title="Spukify Backend",
    description="This is the backend for the Spukify project",
)

"""
SPUKIFY BACKEND
    This is the main file of the project.
    It setups the FASTAPI application and includes the routers.
    It also creates the database tables.
"""

# Create the database tables
track_model.Base.metadata.create_all(bind=engine)
user_model.Base.metadata.create_all(bind=engine)
album_model.Base.metadata.create_all(bind=engine)
artist_model.Base.metadata.create_all(bind=engine)

# Add the middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Include the routers
app.include_router(users_router.users_router)
app.include_router(artists_router.artists_router)


# Redirect to the documentation
@app.get("/", include_in_schema=False)
async def index():
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
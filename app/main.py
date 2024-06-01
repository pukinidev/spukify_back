# Server 
import uvicorn

# FastAPI imports
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse
from api import user_api

app = FastAPI(
    title="Spukify Backend",
    description="This is the backend for the Spukify project",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

# Define the API routes
app.mount("/users", user_api.usersapi)

# Redirect to /docs
@app.get("/users", include_in_schema=False)
async def redirect_to_docs():
    return RedirectResponse(url="users/docs")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
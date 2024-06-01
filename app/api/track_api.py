from fastapi import FastAPI
from fastapi import FastAPI, Depends
from config.database import get_db
from sqlalchemy.orm import Session
from models import track_model
from config.database import engine

tracksapi = FastAPI()



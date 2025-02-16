import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from dotenv import load_dotenv
from models.main_models import Base

# Load environment variables from .env file
load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
        DATABASE_URL,
        pool_size=100,
        max_overflow=10,
    )

# Session management
SessionFactory = sessionmaker(bind=engine)
Session = scoped_session(SessionFactory)

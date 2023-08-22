from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace this with the desired path for your SQLite database file
DATABASE_URL = "postgresql://postgre:Sanchitpsql@localhost/adviNow"
engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

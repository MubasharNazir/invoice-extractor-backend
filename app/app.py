from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.database import engine, get_db, Base
from app.models import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI with PostgreSQL!"}

@app.post("/users/")
def create_user(name: str, email: str, db: Session = Depends(get_db)):
    user = User(name=name, email=email)
    db.add(user)
    db.commit()
    db.refresh(user)
    return {"id": user.id, "name": user.name, "email": user.email}

@app.get("/users/")
def read_all_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users
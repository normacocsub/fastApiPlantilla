from fastapi import APIRouter, Depends
from app.models.user import User
from typing import List
from app.database import Base, engine, get_db

router = APIRouter()

@router.post("/", response_model=User, status_code=201)
def create_user(user_create: User, db: Session = Depends(get_db)):
    db_user = User.find_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    db_user = User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/", response_model=List[User], status_code=200)
def read_users(skip: int = 0, limit: int = 100):
    # código para obtener una lista de usuarios
    users = []
    return users

@router.get("/{user_id}", response_model=User, status_code=200)
def read_user(user_id: int):
    # código para obtener un usuario por su ID
    return user

@router.put("/{user_id}", response_model=User, status_code=200)
def update_user(user_id: int, user_update: UserUpdate):
    # código para actualizar un usuario por su ID
    return user

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int):
    # código para eliminar un usuario por su ID
    return None
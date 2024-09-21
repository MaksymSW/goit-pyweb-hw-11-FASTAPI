from typing import List

from fastapi import Depends, HTTPException, status, Path, APIRouter, Query, Body
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactResponse
from src. repository import search as repository_contacts

search = APIRouter(prefix="/api/search", tags=['search'])


@search.get("/firstname/{firstname}", response_model=ContactResponse)
async def get_contact_firstname(firstname: str = Path(), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_firstname(firstname, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@search.get("/lastname/{lastname}", response_model=ContactResponse)
async def get_contact_lastname(lastname: str = Path(), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_lastname(lastname, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@search.get("/email/{email}", response_model=ContactResponse)
async def get_contact_email(email: str = Path(), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_email(email, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@search.get("/phone/{phone}", response_model=ContactResponse)
async def get_contact_email(phone: str = Path(), db: Session = Depends(get_db)):
    contact = await repository_contacts.get_contact_by_phone(phone, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contact


@search.get("/shift/{shift}", response_model=List[ContactResponse])
async def get_birthday_list(shift: int, db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_birthday_list(shift, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")
    return contacts
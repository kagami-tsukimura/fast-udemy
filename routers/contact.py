from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

import cruds.contact as contact_crud
import schemas.contact as contact_schema
from database import get_db

router = APIRouter(
    prefix="/contacts",
    tags=["contacts"],
)


def get_message():
    message = "Hello World!"
    print(f"message: {message}")
    return message


@router.get("/depends")
async def main(message: str = Depends(get_message)):
    print(f"main: {message}")
    return {"message": message}


@router.get("/", response_model=list[contact_schema.ContactList])
async def get_contact_all(db: AsyncSession = Depends(get_db)):

    return await contact_crud.get_contact_all(db)


@router.post("/", response_model=contact_schema.ContactCreate)
async def create_contact(
    body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    return await contact_crud.create_contact(db, body)


@router.get("/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int, db: AsyncSession = Depends(get_db)):
    contact = await contact_crud.get_contact_by_id(db, id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")
    return contact


@router.put("/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(
    id: int, body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    contact = await contact_crud.get_contact_by_id(db, id)
    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    return contact_crud.update_contact(db, body, original=contact)


@router.delete("/{id}", response_model=None)
async def delete_contact(id: int):
    return

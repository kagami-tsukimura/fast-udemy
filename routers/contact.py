from datetime import datetime

from fastapi import APIRouter, Depends
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
async def get_contact_all():
    dummy_data = datetime.now()

    return [
        contact_schema.ContactBase(
            id=1,
            name="test",
            email="test@test.com",
            url="https://example.com/",
            gender=1,
            message="test",
            is_enabled=True,
            created_at=dummy_data,
        )
    ]


@router.post("/", response_model=contact_schema.ContactCreate)
async def create_contact(
    body: contact_schema.ContactCreate, db: AsyncSession = Depends(get_db)
):
    return await contact_crud.create_contact(db, body)


@router.get("/{id}", response_model=contact_schema.ContactDetail)
async def get_contact(id: int):
    return contact_schema.ContactDetail(id)


@router.put("/{id}", response_model=contact_schema.ContactCreate)
async def update_contact(id: int, body: contact_schema.ContactCreate):
    return contact_schema.ContactCreate(id, **body.model_dump())


@router.delete("/{id}", response_model=None)
async def delete_contact(id: int):
    return

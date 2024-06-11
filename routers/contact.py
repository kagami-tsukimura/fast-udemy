from datetime import datetime

from fastapi import APIRouter

import schemas.contact as contact_schema

router = APIRouter(
    prefix="/contacts",
    tags=["contacts"],
)


@router.get("/", response_model=list[contact_schema.Contact])
async def get_contact_all():
    dummy_data = datetime.now()

    return [
        contact_schema.Contact(
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


@router.post("/", response_model=contact_schema.Contact)
async def create_contact(body: contact_schema.Contact):
    return contact_schema.Contact(**body.model_dump())


@router.get("/{id}")
async def get_contact():
    pass


@router.put("/{id}")
async def update_contact():
    pass


@router.delete("/{id}")
async def delete_contact():
    pass

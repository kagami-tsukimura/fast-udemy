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
            email="test",
            url="test@test.com",
            gender=1,
            message="test",
            is_enabled=True,
            created_at=dummy_data,
        )
    ]


@router.post("/")
async def create_contact():
    pass


@router.get("/{id}")
async def get_contact():
    pass


@router.put("/{id}")
async def update_contact():
    pass


@router.delete("/{id}")
async def delete_contact():
    pass

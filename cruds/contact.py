from sqlalchemy.ext.asyncio import AsyncSession

import models.contact as contact_model
import schemas.contact as contact_schema


async def create_contact(db: AsyncSession, contact: contact_schema.ContactCreate):
    db_contact = contact.model_dump()
    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

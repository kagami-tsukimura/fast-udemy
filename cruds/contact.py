from sqlalchemy.ext.asyncio import AsyncSession

import models.contact as contact_model
import schemas.contact as contact_schema


async def create_contact(
    db: AsyncSession, contact: contact_schema.ContactCreate
) -> contact_model.Contact:
    db_contact = contact.model_dump()
    if db_contact["url"] is not None:
        db_contact["url"] = str(db_contact["url"])
    db.add(db_contact)
    await db.commit()
    await db.refresh(db_contact)
    return db_contact

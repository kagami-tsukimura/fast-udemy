from typing import List, Tuple

from sqlalchemy.ext.asyncio import AsyncSession

import models.contact as contact_model
import schemas.contact as contact_schema


async def create_contact(
    db: AsyncSession, contact: contact_schema.ContactCreate
) -> contact_model.Contact:
    """
    Create DB Contact
    Args:
        db: AsyncSession
        contact: contact_schema.ContactCreate
    Returns:
        contact_model.Contact
    """

    db_contact = contact.model_dump()
    if db_contact["url"]:
        db_contact["url"] = str(db_contact["url"])

    sql_db = contact_model.Contact(**db_contact)
    db.add(sql_db)
    await db.commit()
    await db.refresh(sql_db)
    return sql_db

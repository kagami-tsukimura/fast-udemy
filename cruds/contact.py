from datetime import datetime
from typing import List, Tuple

from sqlalchemy import select
from sqlalchemy.engine import Result
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


async def get_contact_all(db: AsyncSession) -> List[Tuple[int, str, datetime]]:
    """
    Get all contacts
    Args:
        db: AsyncSession
    Returns:
        List[Tuple[int, str, datetime]]
    """

    query = select(contact_model.Contact)
    result: Result = await db.execute(query)
    return result.all()

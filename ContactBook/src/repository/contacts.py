from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.schemas.contact import ContactResponse, ContactSchema
from src.database.models import Contact


async def create_contact(body: ContactSchema, db: AsyncSession):
    contact = Contact(**body.model_dump(exclude_unset=True))
    db.add(contact)
    await db.commit()
    await db.refresh(contact)
    return contact


async def get_contacts(limit: int, offset: int, db: AsyncSession):
    pass


async def get_contact(contact_id: int, db: AsyncSession) -> ContactResponse:
    pass


async def update_contact(contact_id: int, db: AsyncSession):
    pass


async def delete_contact(contact_id: int, db: AsyncSession):
    pass

from fastapi import APIRouter, Depends, Query, HTTPException, status, Path
from sqlalchemy.ext.asyncio import AsyncSession

from src.database.db import get_db
from src.repository import contacts as repositories_contacts
from src.schemas.contact import ContactResponse, ContactSchema

router = APIRouter(prefix='/contacts', tags=['contacts'])


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactSchema, db: AsyncSession = Depends(get_db)):
    return await repositories_contacts.create_contact(body, db)


@router.get('/', response_model=list[ContactResponse])
async def get_contacts(limit: int = Query(10, ge=10, le=500),
                       offset: int = Query(0, ge=0),
                       db: AsyncSession = Depends(get_db)):
    return await repositories_contacts.get_contacts(limit, offset, db)


@router.get("/search", response_model=list[ContactResponse])
async def search_contacts(first_name: str = Query(None), last_name: str = Query(None), email: str = Query(None),
                          db: AsyncSession = Depends(get_db)):
    return await repositories_contacts.search(first_name, last_name, email, db)


@router.get("/birthdays/", response_model=list[ContactResponse])
async def get_birthdays(db: AsyncSession = Depends(get_db)):
    return await repositories_contacts.upcoming_birthday(db)


@router.get('/{contact_id}', response_model=ContactResponse)
async def get_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.get_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {contact_id} not found')
    return contact


@router.put('/{contact_id}')
async def update_contact(body: ContactSchema, contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.update_contact(contact_id, body, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {contact_id} not found')
    return contact


@router.delete("/{contact_id}")
async def delete_contact(contact_id: int = Path(ge=1), db: AsyncSession = Depends(get_db)):
    contact = await repositories_contacts.delete_contact(contact_id, db)
    if contact is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Contact with id {contact_id} not found')
    return contact

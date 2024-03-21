from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    first_name: Mapped[str] = mapped_column(String(100), index=True)
    last_name: Mapped[str] = mapped_column(String(100), index=True)
    email: Mapped[str] = mapped_column(String(100), index=True, nullable=True)
    phone_number: Mapped[str] = mapped_column(String(20), index=True, unique=True)
    birthday: Mapped[str] = mapped_column(Date, nullable=True, index=True)
    description: Mapped[str] = mapped_column(String(250), nullable=True, index=True)

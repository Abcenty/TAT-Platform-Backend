import uuid
from uuid import UUID

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from vitacore_service.infra.db.models import Base


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    snils: Mapped[str | None] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    gender: Mapped[str] = mapped_column()
    birth_date: Mapped[str] = mapped_column()
    documents: Mapped[list[dict]] = mapped_column(JSONB)
    address: Mapped[list[dict]] = mapped_column(JSONB)
    monitoring: Mapped[list[dict] | None] = mapped_column(JSONB)
    contacts: Mapped[list[dict | None]] = mapped_column(JSONB)

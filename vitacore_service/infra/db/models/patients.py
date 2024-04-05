import uuid
from uuid import UUID

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from vitacore_service.infra.db.models import Base


class Patient(Base):
    __tablename__ = "patient"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    snils: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=False)
    gender: Mapped[str] = mapped_column(nullable=False)
    birth_date: Mapped[str] = mapped_column(nullable=False)
    documents: Mapped[list[dict]] = mapped_column(JSONB, nullable=False)
    address: Mapped[list[dict]] = mapped_column(JSONB, nullable=False)
    monitoring: Mapped[list[dict] | None] = mapped_column(JSONB, nullable=True)
    contacts: Mapped[list[dict]] = mapped_column(JSONB, nullable=False)

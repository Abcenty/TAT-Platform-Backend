import uuid
from datetime import date
from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vitacore_service.infra.db.models import Base


if TYPE_CHECKING:
    from vitacore_service.infra.db.models import Position


class Worker(Base):
    __tablename__ = "worker"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    snils: Mapped[str] = mapped_column(nullable=False)
    last_name: Mapped[str] = mapped_column(nullable=False)
    first_name: Mapped[str] = mapped_column(nullable=False)
    middle_name: Mapped[str] = mapped_column(nullable=False)
    birth_date: Mapped[date] = mapped_column(nullable=False)
    date_begin: Mapped[date | None] = mapped_column(nullable=True)
    date_end: Mapped[date | None] = mapped_column(nullable=True)
    contacts: Mapped[list[dict]] = mapped_column(JSONB, nullable=False)

    positions: Mapped[list["Position"]] = relationship(back_populates="worker")

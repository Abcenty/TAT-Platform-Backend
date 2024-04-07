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
    snils: Mapped[str] = mapped_column()
    last_name: Mapped[str] = mapped_column()
    first_name: Mapped[str] = mapped_column()
    middle_name: Mapped[str] = mapped_column()
    birth_date: Mapped[date] = mapped_column()
    date_begin: Mapped[date | None] = mapped_column()
    date_end: Mapped[date | None] = mapped_column()
    contacts: Mapped[list[dict]] = mapped_column(JSONB)

    positions: Mapped[list["Position"]] = relationship(back_populates="worker")

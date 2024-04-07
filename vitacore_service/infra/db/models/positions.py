import uuid
from datetime import date
from uuid import UUID
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from vitacore_service.infra.db.models import Base


if TYPE_CHECKING:
    from vitacore_service.infra.db.models import Department, Worker


class Position(Base):
    __tablename__ = "position"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    date_begin: Mapped[date] = mapped_column(nullable=False)
    department_id: Mapped[UUID] = mapped_column(
        ForeignKey("department.id"),
        nullable=False,
    )
    department_name: Mapped[str] = mapped_column(nullable=False)
    position_name: Mapped[str] = mapped_column(nullable=False)
    position_rate: Mapped[str | None] = mapped_column(nullable=True)
    position_fed_code: Mapped[str] = mapped_column(nullable=False)
    position_reg_name: Mapped[str | None] = mapped_column(nullable=True)
    position_speciality_code: Mapped[str | None] = mapped_column(nullable=True)
    position_speciality_name: Mapped[str | None] = mapped_column(nullable=True)

    worker_id: Mapped[UUID] = mapped_column(ForeignKey("worker.id"), nullable=False)

    department: Mapped["Department"] = relationship()
    worker: Mapped["Worker"] = relationship(back_populates="positions")

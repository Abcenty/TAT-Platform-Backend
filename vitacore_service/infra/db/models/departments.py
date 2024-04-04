from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import JSONB

from vitacore_service.infra.db.models.base import Base


class Department(Base):
    __tablename__ = 'department'

    id: Mapped[UUID] = mapped_column(primary_key=True)
    parent_id: Mapped[UUID | None] = mapped_column(ForeignKey('department.id'))
    code: Mapped[str] = mapped_column(nullable=False)
    fullname: Mapped[str] = mapped_column(nullable=False)
    shortname: Mapped[str] = mapped_column(nullable=False)
    type: Mapped[str] = mapped_column(nullable=False)
    inn: Mapped[str] = mapped_column(nullable=False)
    kpp: Mapped[str] = mapped_column(nullable=False)
    ogrn: Mapped[str] = mapped_column(nullable=False)
    address: Mapped[dict] = mapped_column(JSONB)
    contacts: Mapped[dict] = mapped_column(JSONB)

    parent: Mapped['Department'] = relationship('Department')

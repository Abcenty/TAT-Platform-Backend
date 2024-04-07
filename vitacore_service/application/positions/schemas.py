from datetime import date
from typing import Any, Annotated
from uuid import UUID

from pydantic import BaseModel, Field


class PositionRead(BaseModel):
    id: Annotated[
        UUID,
        Field(description="Идентификатор сотрудника в связке с должностью"),
    ]
    dateBegin: Annotated[date, Field(description="Дата начала работы")]
    departmentId: Annotated[UUID, Field(description="Идентификатор МО / филиала")]
    departmentName: Annotated[str, Field(description="Наименование МО / филиала")]
    positionName: Annotated[
        str,
        Field(description="Тип должности. Наименование (смотри док-ю VitaCore)"),
    ]
    positionRate: Annotated[Any, Field(description="Число, количество ставок")] = None
    positionFedCode: Annotated[
        str,
        Field(description="Тип должности. Код (смотри док-ю VitaCore)"),
    ]
    positionRegName: Annotated[
        str | None,
        Field(description="ФРМР. Должности медицинского персонала"),
    ]
    positionSpecialityCode: Annotated[
        str | None,
        Field(
            description="Код специальности по справочнику V021. "
            "Классификатор медицинских специальностей (справочник ТФОМС)",
        ),
    ] = None
    positionSpecialityName: Annotated[
        str | None,
        Field(description="Наименование специальности по справочнику V021"),
    ] = None

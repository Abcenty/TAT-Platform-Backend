from datetime import date
from uuid import UUID

from vitacore_service.application.common.workers_gateway import WorkerReader
from vitacore_service.domain.models.positions import PositionDTO
from vitacore_service.domain.models.workers import WorkerDTO


class MockWorkersGateway(WorkerReader):
    async def get_by_department(self, department_id: UUID) -> list[WorkerDTO]:
        mock_data = [
            WorkerDTO(
                id="a162bc67-c5ed-4139-863f-930a5e29d0e8",
                snils="123",
                last_name="surname1",
                first_name="name1",
                middle_name="",
                birth_date=date(2000, 1, 1),
                date_begin=date(2020, 1, 1),
                date_end=None,
                positions=[
                    PositionDTO(
                        id="5206b9f8-5aca-455a-9da9-25cc84811615",
                        date_begin=date(2020, 1, 1),
                        department_id="68128df8-0194-4437-b8a0-72fed2cf9904",
                        department_name="test",
                        position_name="test",
                        position_rate="",
                        position_fed_code="",
                        position_reg_name="",
                        position_speciality_code="",
                        position_speciality_name="",
                        worker_id="a162bc67-c5ed-4139-863f-930a5e29d0e8",
                    ),
                    PositionDTO(
                        id="5106b9f8-5aca-455a-9da9-25cc84811615",
                        date_begin=date(2022, 1, 1),
                        department_id="68128df8-0194-4437-b8a0-72fed2cf9904",
                        department_name="test",
                        position_name="test2",
                        position_rate="",
                        position_fed_code="",
                        position_reg_name="",
                        position_speciality_code="",
                        position_speciality_name="",
                        worker_id="a162bc67-c5ed-4139-863f-930a5e29d0e8",
                    ),
                ],
                contacts=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
            ),
            WorkerDTO(
                id="852cad40-784d-4ba9-8955-f388b2488cf1",
                snils="321",
                last_name="surname2",
                first_name="name2",
                middle_name="",
                birth_date=date(2002, 1, 1),
                date_begin=date(2022, 1, 1),
                date_end=None,
                positions=[
                    PositionDTO(
                        id="5306b9f8-5aca-455a-9da9-25cc84811615",
                        date_begin=date(2022, 1, 1),
                        department_id="74128df8-0194-4437-b8a0-72fed2cf9904",
                        department_name="test2",
                        position_name="test3",
                        position_rate="",
                        position_fed_code="",
                        position_reg_name="",
                        position_speciality_code="",
                        position_speciality_name="",
                        worker_id="a162bc67-c5ed-4139-863f-930a5e29d0e8",
                    ),
                ],
                contacts=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
            ),
        ]

        return mock_data

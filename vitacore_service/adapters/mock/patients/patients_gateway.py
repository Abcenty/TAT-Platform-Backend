import random
from uuid import UUID

from vitacore_service.application.common.patients_gateway import PatientReader
from vitacore_service.domain.models.patients import PatientDTO


class MockPatientsGateway(PatientReader):
    async def get(self, patient_id: UUID) -> PatientDTO:
        return PatientDTO(
            id=patient_id,
            snils=str(random.randint(100, 1000)),
            last_name="test",
            first_name="test",
            middle_name="test",
            gender="male",
            birth_date="01.01.2000",
            documents=[
                {
                    "type": "test",
                    "display": "test",
                },
            ],
            address=[
                {
                    "type": "test",
                    "display": "test",
                },
            ],
            monitoring=[
                {
                    "type": "test",
                    "display": "test",
                },
            ],
            contacts=[
                {
                    "type": "test",
                    "display": "test",
                },
            ],
        )

    async def find(
        self,
        findstr: str | None,
        snils: str | None,
        docnum: str | None,
    ) -> list[PatientDTO]:
        return [
            PatientDTO(
                id="132ae70c-5177-4c6a-be27-6eaee88d8563",
                snils=str(random.randint(100, 1000)),
                last_name="test",
                first_name="test",
                middle_name="test",
                gender="male",
                birth_date="01.01.2000",
                documents=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
                address=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
            ),
            PatientDTO(
                id="222ae70c-5177-4c6a-be27-6eaee88d8222",
                last_name="test",
                first_name="test",
                middle_name="test",
                gender="male",
                birth_date="01.01.2000",
                documents=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
                address=[
                    {
                        "type": "test",
                        "display": "test",
                    },
                ],
            ),
        ]

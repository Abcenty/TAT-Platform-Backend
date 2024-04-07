from uuid import UUID

from aiohttp import ClientSession

from vitacore_service.adapters.http.patients.patients_converter import (
    dict_to_patient_dto,
)
from vitacore_service.infra.config import Settings
from vitacore_service.application.common.patients_gateway import PatientReader
from vitacore_service.domain.models.patients import PatientDTO


class HttpPatientsGateway(PatientReader):
    def __init__(self, session: ClientSession, settings: Settings):
        self.session = session
        self.vitacore_url = settings.vitacore_url

    async def get(self, patient_id: UUID) -> PatientDTO:
        url = self.vitacore_url + f"forTis/patient?patId={patient_id}"

        async with self.session.get(url) as response:
            if not response.ok:
                raise Exception

            result = await response.json()

        return dict_to_patient_dto(result)

    async def find(
        self,
        findstr: str | None,
        snils: str | None,
        docnum: str | None,
    ) -> list[PatientDTO]:
        url = self.vitacore_url + "forTis/find_patients"

        params = dict()
        if findstr is not None:
            params["findstr"] = findstr
        if snils is not None:
            params["snils"] = snils
        if docnum is not None:
            params["docnum"] = docnum

        async with self.session.get(url, params=params) as response:
            if not response.ok:
                raise Exception

            result = await response.json()

        return [dict_to_patient_dto(patient_dict) for patient_dict in result]
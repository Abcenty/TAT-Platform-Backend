from vitacore_service.application.common.interactor import Interactor
from vitacore_service.application.common.patients_gateway import (
    PatientReader,
    PatientSaver,
)
from vitacore_service.application.common.uow import UoW
from vitacore_service.application.patients.converter import patient_dto_to_response
from vitacore_service.application.patients.schemas import (
    FindPatientsRequest,
    PatientRead,
)


class FindPatients(Interactor[FindPatientsRequest, list[PatientRead]]):
    def __init__(
        self,
        http_patients_reader: PatientReader,
        db_patients_saver: PatientSaver,
        uow: UoW,
    ):
        self.http_patients_reader = http_patients_reader
        self.db_patients_saver = db_patients_saver
        self.uow = uow

    async def __call__(self, data: FindPatientsRequest) -> list[PatientRead]:
        patients = await self.http_patients_reader.find(
            findstr=data.findstr,
            snils=data.snils,
            docnum=data.docnum,
        )

        await self.db_patients_saver.save_bulk(patients)
        await self.uow.commit()

        return [patient_dto_to_response(patient) for patient in patients]

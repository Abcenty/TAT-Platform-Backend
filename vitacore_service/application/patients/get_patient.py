from vitacore_service.application.common.interactor import Interactor
from vitacore_service.application.common.patients_gateway import (
    PatientReader,
    PatientSaver,
)
from vitacore_service.application.common.uow import UoW
from vitacore_service.application.patients.converter import patient_dto_to_response
from vitacore_service.application.patients.schemas import (
    GetPatientRequest,
    PatientRead,
)
from vitacore_service.domain.services.patients import PatientsService


class GetPatient(Interactor[GetPatientRequest, PatientRead]):
    def __init__(
        self,
        http_patients_reader: PatientReader,
        db_patients_saver: PatientSaver,
        patients_service: PatientsService,
        uow: UoW,
    ):
        self.http_patients_reader = http_patients_reader
        self.db_patients_saver = db_patients_saver
        self.patients_service = patients_service
        self.uow = uow

    async def __call__(self, data: GetPatientRequest) -> PatientRead:
        patient = await self.http_patients_reader.get(data.patient_id)

        patient = self.patients_service.create(
            id=patient.id,
            snils=patient.snils,
            last_name=patient.last_name,
            first_name=patient.first_name,
            middle_name=patient.middle_name,
            gender=patient.gender,
            birth_date=patient.birth_date,
            documents=patient.documents,
            address=patient.address,
            contacts=patient.monitoring,
            monitoring=patient.contacts,
        )

        await self.db_patients_saver.save_with_update(patient)
        await self.uow.commit()

        return patient_dto_to_response(patient)

from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from vitacore_service.adapters.db.patients.patients_coverter import patient_dto_to_db
from vitacore_service.infra.db.models import Patient
from vitacore_service.application.common.patients_gateway import PatientSaver
from vitacore_service.domain.models.patients import PatientDTO


class DBPatientsGateway(PatientSaver):
    def __init__(self, session: AsyncSession):
        self.session = session

    async def save(self, patient: PatientDTO) -> None:
        """
        Adds patient to the database. When there is a conflict, an update occurs.

        !!! Used insert from postgresql dialect, when changing the DBMS, you will have to update this method
        """
        db_patient = patient_dto_to_db(patient)

        stmt = insert(Patient).values(
            {
                "id": db_patient.id,
                "snils": db_patient.snils,
                "last_name": db_patient.last_name,
                "first_name": db_patient.first_name,
                "middle_name": db_patient.middle_name,
                "gender": db_patient.gender,
                "birth_date": db_patient.birth_date,
                "documents": db_patient.documents,
                "address": db_patient.address,
                "monitoring": db_patient.monitoring,
                "contacts": db_patient.contacts,
            },
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[Patient.id],
            set_={
                "snils": stmt.excluded.snils,
                "last_name": stmt.excluded.last_name,
                "first_name": stmt.excluded.first_name,
                "middle_name": stmt.excluded.middle_name,
                "gender": stmt.excluded.gender,
                "birth_date": stmt.excluded.birth_date,
                "documents": stmt.excluded.documents,
                "address": stmt.excluded.address,
                "monitoring": stmt.excluded.monitoring,
                "contacts": stmt.excluded.contacts,
            },
        )

        await self.session.execute(stmt)

    async def save_bulk(self, patients: list[PatientDTO]) -> None:
        """
        Adds several patients to the database. When there is a conflict, an update occurs.

        !!! Used insert from postgresql dialect, when changing the DBMS, you will have to update this method
        """
        db_patients = [patient_dto_to_db(patient) for patient in patients]

        stmt = insert(Patient).values(
            [
                {
                    "id": db_patient.id,
                    "snils": db_patient.snils,
                    "last_name": db_patient.last_name,
                    "first_name": db_patient.first_name,
                    "middle_name": db_patient.middle_name,
                    "gender": db_patient.gender,
                    "birth_date": db_patient.birth_date,
                    "documents": db_patient.documents,
                    "address": db_patient.address,
                    "monitoring": db_patient.monitoring,
                    "contacts": db_patient.contacts,
                }
                for db_patient in db_patients
            ],
        )

        stmt = stmt.on_conflict_do_update(
            index_elements=[Patient.id],
            set_={
                "snils": stmt.excluded.snils,
                "last_name": stmt.excluded.last_name,
                "first_name": stmt.excluded.first_name,
                "middle_name": stmt.excluded.middle_name,
                "gender": stmt.excluded.gender,
                "birth_date": stmt.excluded.birth_date,
                "documents": stmt.excluded.documents,
                "address": stmt.excluded.address,
                "monitoring": stmt.excluded.monitoring,
                "contacts": stmt.excluded.contacts,
            },
        )

        await self.session.execute(stmt)

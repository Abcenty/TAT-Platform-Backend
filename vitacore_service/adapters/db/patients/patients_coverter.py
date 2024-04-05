from vitacore_service.domain.models.patients import PatientDTO
from vitacore_service.infra.db.models import Patient


def patient_dto_to_db(patient: PatientDTO) -> Patient:
    return Patient(
        id=patient.id,
        snils=patient.snils,
        last_name=patient.last_name,
        first_name=patient.first_name,
        middle_name=patient.middle_name,
        gender=patient.gender,
        birth_date=patient.birth_date,
        documents=patient.documents,
        address=patient.address,
        monitoring=patient.monitoring,
        contacts=patient.contacts,
    )


def patient_db_to_dto(patient: Patient) -> PatientDTO:
    return PatientDTO(
        id=patient.id,
        snils=patient.snils,
        last_name=patient.last_name,
        first_name=patient.first_name,
        middle_name=patient.middle_name,
        gender=patient.gender,
        birth_date=patient.birth_date,
        documents=patient.documents,
        address=patient.address,
        monitoring=patient.monitoring,
        contacts=patient.contacts,
    )

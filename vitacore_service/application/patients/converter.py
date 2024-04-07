from vitacore_service.application.patients.schemas import PatientRead
from vitacore_service.domain.models.patients import PatientDTO


def patient_dto_to_response(patient: PatientDTO) -> PatientRead:
    return PatientRead(
        id=patient.id,
        SNILS=patient.snils,
        lastName=patient.last_name,
        firstName=patient.first_name,
        middleName=patient.middle_name,
        gender=patient.gender,
        birthDate=patient.birth_date,
        documents=patient.documents,
        address=patient.address,
        monitoring=patient.monitoring,
        contacts=patient.contacts,
    )
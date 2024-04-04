from vitacore_service.domain.models.patients import PatientDTO


def dict_to_patient_dto(patient_dict: dict) -> PatientDTO:
    return PatientDTO(
        id=patient_dict.get('id'),
        snils=patient_dict.get('SNILS'),
        last_name=patient_dict.get('lastName'),
        first_name=patient_dict.get('firstName'),
        middle_name=patient_dict.get('middleName'),
        gender=patient_dict.get('gender'),
        birth_date=patient_dict.get('birthDate'),
        documents=patient_dict.get('documents'),
        address=patient_dict.get('address'),
        monitoring=patient_dict.get('monitoring'),
        contacts=patient_dict.get('contacts')
    )

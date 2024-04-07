from vitacore_service.domain.exceptions.base import DomainError


class VitacoreError(DomainError):
    pass


class VitacoreUnreachableError(VitacoreError):
    pass


class VitacoreBadStatusError(VitacoreError):
    pass


class VitacoreBadResponseError(VitacoreError):
    pass

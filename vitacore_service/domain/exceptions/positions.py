from vitacore_service.domain.exceptions.base import DomainError


class PositionBadDepartmentError(DomainError):
    """A department_id is specified that does not exist"""

    pass

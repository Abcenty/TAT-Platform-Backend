from abc import abstractmethod
from typing import Protocol

from vitacore_service.domain.models.positions import PositionDTO


class PositionSaver(Protocol):
    @abstractmethod
    async def bulk_save_with_update(self, positions: list[PositionDTO]):
        raise NotImplementedError


class PositionReader(Protocol):
    pass


class PositionUpdater(Protocol):
    pass

from typing import List
from uuid import UUID

from pydantic import BaseModel


class StatisticsSchema(BaseModel):
    count_patients: int
    count_studies: int
    total_disk_size: int
    count_first_opinion: int
    count_second_opinion: int


class StatisticsOrganizationSchema(BaseModel):
    id: UUID

    name: str
    addresses: List[str]

    device_count: int


class StatisticsOrganizationsSchema(BaseModel):
    total: int
    organizations: List[StatisticsOrganizationSchema]


class StatisticsCountDeviceSchema(BaseModel):
    modality: str
    value: int


class StatisticsAgeDeviceSchema(BaseModel):
    modality: str
    count: int
    group_index: int


class StatisticsCountStudiesDeviceSchema(BaseModel):
    modality: str
    value: int


class StatisticsDevicesSchema(BaseModel):
    count_devices: List[StatisticsCountDeviceSchema]
    age_devices: List[StatisticsAgeDeviceSchema]
    count_studies_devices: List[StatisticsCountStudiesDeviceSchema]

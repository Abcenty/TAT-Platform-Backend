import random

from vitacore_service.application.common.departments_gateway import DepartmentReader
from vitacore_service.domain.models.departments import DepartmentDTO


class MockDepartmentsGateway(DepartmentReader):
    async def get_all(self) -> list[DepartmentDTO]:
        mock_data = [
            DepartmentDTO(
                id='74128df8-0194-4437-b8a0-72fed2cf9904',
                parent_id=None,
                code='100',
                fullname='Test Parent Department',
                shortname='',
                type='test',
                inn='123',
                kpp='123',
                ogrn='123',
                address=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ],
                contacts=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ]
            ),
            DepartmentDTO(
                id='68128df8-0194-4437-b8a0-72fed2cf9904',
                parent_id='74128df8-0194-4437-b8a0-72fed2cf9904',
                code='100',
                fullname='Test Department 1',
                shortname='',
                type='test',
                inn=str(random.randint(100, 1000)),
                kpp='123',
                ogrn='123',
                address=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ],
                contacts=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ]
            ),
            DepartmentDTO(
                id='11128df8-0194-4437-b8a0-72fed2cf9904',
                parent_id=None,
                code='100',
                fullname='Test Department 2',
                shortname='',
                type='test',
                inn='123',
                kpp='123',
                ogrn='123',
                address=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ],
                contacts=[
                    {
                        'type': 'test',
                        'display': 'test'
                    }
                ]
            )
        ]

        return mock_data

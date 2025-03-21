from unittest import TestCase

from app import mongo
from app.data.repository import tenant_repository
from app.data.repository.tenant_repository import TenantRepository
from app.exceptionHandle.tenant_already_exist import TenantAlreadyExistsException
from app.exceptionHandle.invalid_login_details import InvalidLoginDetailsException
from app.mapper.tenant_mapper import TenantMapper
from app.services.tenant_service import TenantServiceInterface
from app.services.tenant_services_implementation import TenantServices


class TestTenantServices(TestCase):

    tenant_repository = TenantRepository(mongo)
    tenant_service: TenantServiceInterface = TenantServices(tenant_repository)
    def setUp(self):
        self.tenant_repository.clear()

    def test_that_tenant_can_register_successfully(self):
        tenant_information = {
            'name': 'Babatunde',
            'room_id': '101',
            'email': 'babatunde@gmail.com',
            'password': '123456'
        }
        self.tenant_service.register_tenant(tenant_information)
        tenant_count = self.tenant_service.get_tenant_count()
        self.assertEqual(1, tenant_count)


    def test_that_error_is_thrown_when_tenant_wants_to_register_twice(self):
        tenant_information = {
            'name': 'Babatunde',
            'room_id': '101',
            'email': 'babatunde@gmail.com',
            'password': '123456'
        }
        self.tenant_service.register_tenant(tenant_information)

        tenant_count = self.tenant_service.get_tenant_count()
        self.assertEqual(1, tenant_count)

        with self.assertRaises(TenantAlreadyExistsException):
            self.tenant_service.register_tenant(tenant_information)


    def test_that_tenant_can_login_after_registering(self):
        tenant_information = {
            'name': 'Babatunde',
            'room_id': '101',
            'email': 'babatunde@gmail.com',
            'password': '123456'
        }
        self.tenant_service.register_tenant(tenant_information)

        tenant_count = self.tenant_service.get_tenant_count()
        self.assertEqual(1, tenant_count)

        tenant_Login_request_information = {
            'email': 'babatunde@gmail.com',
            'password': '123456'
        }
        tenant_information_to_mapper = TenantMapper.map_to_tenant_login_request(tenant_Login_request_information)
        tenant_Login_response = self.tenant_service.tenant_login(tenant_information_to_mapper)

        self.assertEqual(tenant_Login_response.message, "Login Successful")

    def test_that_error_is_thrown_when_tenant_login_credentials_does_not_exist(self):
        tenant_information = {
            'name': 'Babatunde',
            'room_id': '101',
            'email': 'babatunde@gmail.com',
            'password': '123456'
        }
        self.tenant_service.register_tenant(tenant_information)

        tenant_count = self.tenant_service.get_tenant_count()
        self.assertEqual(1, tenant_count)

        tenant_Login_request_information = {
            'email': 'babatunde@gmail.com',
            'password': 'Wrong password'
        }
        tenant_information_to_mapper = TenantMapper.map_to_tenant_login_request(tenant_Login_request_information)

        with self.assertRaises(InvalidLoginDetailsException):
            self.tenant_service.tenant_login(tenant_information_to_mapper)
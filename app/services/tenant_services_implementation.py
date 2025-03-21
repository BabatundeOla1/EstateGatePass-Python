from flask import request
from app.data.models.tenant import Tenant
from app.data.repository.tenant_repository import TenantRepository
from app.dto.request.tenant_login_request import TenantLoginRequest
from app.exceptionHandle.invalid_login_details import InvalidLoginDetailsException
from app.mapper import tenant_mapper
from app.services.tenant_service import TenantServiceInterface
from app.exceptionHandle.tenant_already_exist import TenantAlreadyExistsException


class TenantServices(TenantServiceInterface):

    def __init__(self, tenant_repository: TenantRepository):
        self.tenant_repository = tenant_repository

    def register_tenant(self, tenant_data: dict):
        existing_tenant = self.tenant_repository.find_tenant_by_email(tenant_data['email'])

        if existing_tenant is not None:
            print(f"Existing tenant found: {existing_tenant}")
            raise TenantAlreadyExistsException("Tenant with email {} already exists".format(tenant_data['email']))

        new_tenant = Tenant.from_dictionary(tenant_data)
        return self.tenant_repository.save_tenant(new_tenant)

    def tenant_login(self, tenant_Login_request: TenantLoginRequest):
        existing_tenant = self.tenant_repository.find_tenant_by_email(tenant_Login_request.email)

        if existing_tenant and existing_tenant["password"] == tenant_Login_request.password:
            return tenant_mapper.TenantMapper.map_to_tenant_login_response(existing_tenant)
        else:
            raise InvalidLoginDetailsException("Invalid password or Tenant does nt exist")


    def get_tenant_count(self):
        return self.tenant_repository.get_tenant_count_from_repository()

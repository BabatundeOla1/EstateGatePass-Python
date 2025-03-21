from flask import request
from werkzeug.security import check_password_hash

from app.data.models.tenant import Tenant
from app.data.repository.tenant_repository import TenantRepository
from app.dto.request.tenant_login_request import TenantLoginRequest
from app.dto.request.tenant_register_request import TenantRegisterRequest
from app.exceptionHandle.invalid_login_details import InvalidLoginDetailsException
from app.mapper import tenant_mapper
from app.mapper.tenant_mapper import TenantMapper
from app.services.tenant_service import TenantServiceInterface
from app.exceptionHandle.tenant_already_exist import TenantAlreadyExistsException


class TenantServices(TenantServiceInterface):

    def __init__(self, tenant_repository: TenantRepository):
        self.tenant_repository = tenant_repository

    def register_tenant(self, tenant_register_request: TenantRegisterRequest):
        existing_tenant = self.tenant_repository.find_tenant_by_email(tenant_register_request.email)

        if existing_tenant is not None:
            raise TenantAlreadyExistsException(f"Tenant with email {tenant_register_request.email} already exists")

        new_tenant = Tenant.from_dictionary(tenant_register_request.to_dictionary())
        tenant_register_response = TenantMapper.map_to_tenant_register_response(new_tenant)
        self.tenant_repository.save_tenant(new_tenant)
        return tenant_register_response

    def tenant_login(self, tenant_Login_request: TenantLoginRequest):
        existing_tenant = self.tenant_repository.find_tenant_by_email(tenant_Login_request.email)

        if existing_tenant and existing_tenant["password"] == tenant_Login_request.password:
            return tenant_mapper.TenantMapper.map_to_tenant_login_response(existing_tenant)

        else:
            raise InvalidLoginDetailsException("Invalid password or Tenant does nt exist")


    def get_tenant_count(self):
        return self.tenant_repository.get_tenant_count_from_repository()

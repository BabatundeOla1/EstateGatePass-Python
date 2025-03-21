from flask import request

from app.data.models.tenant import Tenant
from app.data.repository.tenant_repository import TenantRepository
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

    def get_tenant_count(self):
        return self.tenant_repository.get_tenant_count_from_repository()

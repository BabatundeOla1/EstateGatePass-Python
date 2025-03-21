from app.data.models.tenant import Tenant
from app.dto.request.tenant_login_request import TenantLoginRequest
from app.dto.request.tenant_register_request import TenantRegisterRequest
from app.dto.response.tenant_login_response import TenantLoginResponse
from app.dto.response.tenant_register_response import TenantRegisterResponse


class TenantMapper:
    @staticmethod
    def map_to_tenant_login_request(data: dict) -> 'TenantLoginRequest':
        return TenantLoginRequest(data['email'], data['password'])

    @staticmethod
    def map_to_tenant_login_response(tenant: 'Tenant') -> 'TenantLoginResponse':
        if isinstance(tenant, dict):
            tenant = Tenant.from_dictionary(tenant)

        message = "Login Successful"
        return TenantLoginResponse(
            tenant.email,
            message=message
        )

    @staticmethod
    def map_to_tenant_register_request(data: dict) -> 'TenantRegisterRequest':
        return TenantRegisterRequest(
            name=data['name'],
            room_id=data['room_id'],
            email=data['email'],
            password=data['password']
        )

    @staticmethod
    def map_to_tenant_register_response(tenant: 'Tenant') -> 'TenantRegisterResponse':
        if isinstance(tenant, dict):
            tenant = Tenant.from_dictionary(tenant)

        message = "Register Successful"
        return TenantRegisterResponse(
            tenant.name,
            message=message
        )

from app.data.models.tenant import Tenant
from app.dto.request.tenant_login_request import TenantLoginRequest
from app.dto.response.tenant_login_response import TenantLoginResponse


class TenantMapper:
    @staticmethod
    def map_to_tenant_login_request(data: dict) -> 'TenantLoginRequest':
        return TenantLoginRequest(data['email'], data['password'])

    @staticmethod
    def map_to_tenant_login_response(tenant: 'Tenant') -> 'TenantLoginResponse':
        message = "Login Successful"
        return TenantLoginResponse(
            tenant.email,
            message
        )

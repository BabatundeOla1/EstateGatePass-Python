from abc import ABC, abstractmethod

from app.dto.request.tenant_login_request import TenantLoginRequest
from app.dto.request.tenant_register_request import TenantRegisterRequest


class TenantServiceInterface(ABC):

    @abstractmethod
    def register_tenant(self, tenant_register_request: TenantRegisterRequest):
        pass

    @abstractmethod
    def get_tenant_count(self):
        pass

    @abstractmethod
    def tenant_login(self, tenant_Login_request: TenantLoginRequest):
        pass
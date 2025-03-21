from abc import ABC, abstractmethod

from app.dto.request.tenant_login_request import TenantLoginRequest


class TenantServiceInterface(ABC):

    @abstractmethod
    def register_tenant(self, tenant_data: dict):
        pass

    @abstractmethod
    def get_tenant_count(self):
        pass

    @abstractmethod
    def tenant_login(self, tenant_Login_request: TenantLoginRequest):
        pass
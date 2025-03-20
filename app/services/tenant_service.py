from abc import ABC, abstractmethod

class TenantServiceInterface(ABC):

    @abstractmethod
    def register_tenant(self, tenant_data: dict):
        pass

    @abstractmethod
    def get_tenant_count(self):
        pass
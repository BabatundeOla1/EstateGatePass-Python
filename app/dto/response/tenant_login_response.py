from dataclasses import dataclass


@dataclass
class TenantLoginResponse:

    tenant_id: str
    message: str

    def to_dict(self):
        return {
            "tenant_id": self.tenant_id,
            "message": self.message
        }

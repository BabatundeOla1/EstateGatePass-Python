from dataclasses import dataclass


@dataclass
class TenantLoginResponse:

    tenant_id: str
    email: str
    message: str

    def to_dict(self):
        return {
            "tenant_id": self.tenant_id,
            "email": self.email,
            "message": self.message
        }

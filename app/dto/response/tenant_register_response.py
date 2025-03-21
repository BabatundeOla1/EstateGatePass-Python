from dataclasses import dataclass


@dataclass
class TenantRegisterResponse:
    name: str
    message: str

    def to_dictionary(self):
        return {
            'name': self.name,
            'message': self.message
        }